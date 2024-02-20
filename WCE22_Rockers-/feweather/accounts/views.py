from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
import mysql.connector
import itertools

# Create your views here.
mydb = mysql.connector.connect(
        user="wce22_jango",
        password="jango@123",
        database="wce22_fedbmiraj",
        host="162.240.33.255",
        raise_on_warnings=True,
)

def accounts(request):
    """Accounts Home Page.
    Displays the Button Links to all the forms related to accounts."""
    return render(request, "accounts/accounts.html")

def inwardRemitance(request):
    """Method to render the Inward Remitance Form and Extract and Insert data into rel_invoice_brc Table in database"""

    if request.method == "POST":

        cursor = mydb.cursor()

        sender = request.POST.get("sender") #partyShortName
        currency = request.POST.get("currency")
        forexCur = request.POST.get("forexCur")
        date = request.POST.get("date")
        invoiceNos = request.POST.getlist("invoiceNo[]")
        amountVal = request.POST.getlist("amount[]")
        refs = request.POST.getlist("ref[]")
        entryUser = request.POST.get("entryUser")

        # Inserting all the values into the table
        for (invoiceNo, amount, ref) in zip(invoiceNos, amountVal, refs):
            query = "INSERT INTO rel_invoice_brc (Sender, invoiceNo, Currency, forexCurrency, amount, REF, inwardRemDate, submittedBy) values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}');".format(sender, invoiceNo, currency, forexCur, amount, ref, date, entryUser)
            cursor.execute(query)
            mydb.commit()
        
        cursor.close()
        return redirect('inwardRemitanceTable')

    cursor = mydb.cursor()
    query = "select foreignBuyerCode from foreignbuyer"
    cursor.execute(query)
    partyShortName = cursor.fetchall()

    # query to select the currency from currency table
    query = "select * from currency;"
    cursor.execute(query)
    currencies = cursor.fetchall()


    query = "select invoiceNo, partyShortName from export;"
    cursor.execute(query)
    invoiceAndParty = cursor.fetchall()
    cursor.close()

    # create a context for rendering
    data = {}
    data["partyShortName"] = partyShortName
    data["currencies"] = currencies
    data["invoiceAndParty"] = invoiceAndParty

    return render(request, "accounts/inwardRemitance.html", data)

def inwardRemitanceTable(request):
    mycursor = mydb.cursor()
    query = "SELECT Sender, invoiceNo, Currency, forexCurrency, amount, REF, inwardRemDate, submittedBy, brcNo, brcAmt, brcDate from rel_invoice_brc;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    mycursor.close()
    data = {
        'rel_invoice_brc' : myresult
    }
    return render(request, "accounts/inwardRemitanceTable.html",data)

def brc(request):
    """Method to render and process the BRC form"""

    if request.method=="POST":
        cursor = mydb.cursor()
        invoiceNo = request.POST.get("invoiceNo")
        brcNos = request.POST.getlist("brcNo[]")
        amounts = request.POST.getlist("amount[]")
        dates = request.POST.getlist("date[]")

        # traversing the three lists at once using the zip function and updating values in table to corresponding invoices
        for (brcNo, amount, date) in zip(brcNos, amounts, dates):
            query = "UPDATE rel_invoice_brc SET brcNo='{0}', brcAmt='{1}', brcDate='{2}' WHERE invoiceNo='{3}';".format(brcNo, amount, date, invoiceNo)
            cursor.execute(query)
            mydb.commit()

        cursor.close()
        return redirect('brcTable')

    # select only the invoices which were filled through the inward Remitance form
    cursor = mydb.cursor()
    query = "select invoiceNo from rel_invoice_brc;"
    cursor.execute(query)
    invoiceNos = cursor.fetchall()
    cursor.close()

    data = {}

    data["invoiceNos"] = invoiceNos
    return render(request, "accounts/brc.html", data)

def brcTable(request):
    mycursor = mydb.cursor()
    query = "SELECT Sender, invoiceNo, Currency, forexCurrency, amount, REF, inwardRemDate, submittedBy, brcNo, brcAmt, brcDate from rel_invoice_brc;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    mycursor.close()
    data = {
        'brc' : myresult
    }
    return render(request, "accounts/brcTable.html",data)

def docBank(request):

    cursor = mydb.cursor()

    if request.method == "POST":
        # print(request.POST)
        invoiceNos = request.POST.getlist("invoiceNo[]")
        dates = request.POST.getlist("date[]")
        submittedBy = request.POST.getlist("submittedBy[]")

        for (invoiceNo, date, submissionPerson) in zip(invoiceNos, dates, submittedBy):
            query = "UPDATE exportdocs SET DateOfDocSubToBank='{0}', submittedBy='{1}' where invoiceNo='{2}';".format(date, submissionPerson, invoiceNo)
            cursor.execute(query)
            mydb.commit()

        cursor.close()
        return redirect('docBankTable')


    query = "select invoiceNo from exportdocs;"
    cursor.execute(query)
    invoiceNos = cursor.fetchall()
    cursor.close()

    data = {}

    data["invoiceNos"] = invoiceNos

    return render(request, "accounts/docBank.html", data)

def docBankTable(request):
    mycursor = mydb.cursor()
    query = "SELECT invoiceNo, shippingBillNumber, shippingBillDate, DateOfDocSubToBank, submittedBy from exportdocs;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    mycursor.close()
    data = {
        'docBank' : myresult
    }
    return render(request, "accounts/docBankTable.html",data)

def billOceanTptCha(request):
    # Changes to be made
    cursor = mydb.cursor()

    if request.method == "POST":
        print(request.POST)
        billType = request.POST.get("billType")
        invoiceNo = request.POST.get("invoiceNo")
        containerNo = request.POST.get("containerNo")
        serviceParty = request.POST.get("serviceParty")
        servicePartyOther = request.POST.get("servicePartyOther")
        invoiceBillNo = request.POST.get("invoiceBillNo")
        amount = request.POST.get("amount")
        invDate = request.POST.get("invDate")
        remark = request.POST.get("remark")

        if servicePartyOther != None:
            query = "INSERT into billOceanTptCha (invoiceNo, billType, serviceParty, servicePartyOther, invoiceBillNo, amount, invoiceDate, remark) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}');".format(invoiceNo, billType, serviceParty, servicePartyOther, invoiceBillNo, amount, invDate, remark)
            cursor.execute(query)
            mydb.commit()
        else:
            query = "INSERT into billOceanTptCha (invoiceNo, billType, serviceParty, invoiceBillNo, amount, invoiceDate, remark) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}');".format(invoiceNo, billType, serviceParty, invoiceBillNo, amount, invDate, remark)
            cursor.execute(query)
            mydb.commit()
        cursor.close()
        return redirect('billOceanTptChaTable')


    query = "select * from export;"
    cursor.execute(query)
    invoiceNos = cursor.fetchall()

    query = "select tptName from transporter;"
    cursor.execute(query)
    transporters = cursor.fetchall()

    query = "select agent from chagent;"
    cursor.execute(query)
    chAgents = cursor.fetchall()

    query = "select shippingLineCode from shippingline;"
    cursor.execute(query)
    shippingLineCodes = cursor.fetchall()

    cursor.close()

    data = {}

    data["invoiceNos"] = invoiceNos
    data["transporters"] = transporters
    data["chAgents"] = chAgents
    data["shippingLineCodes"] = shippingLineCodes

    return render(request, "accounts/billOceanTptCha.html", data)

def billOceanTptChaTable(request):
    mycursor = mydb.cursor()
    query = "SELECT invoiceNo, billType, serviceParty, servicePartyOther, invoiceBillNo, amount, invoiceDate, remark from billOceanTptCha;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    mycursor.close()
    data = {
        'billOcean' : myresult
    }
    return render(request, "accounts/billOceanTptChaTable.html",data)