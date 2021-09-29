import mysql.connector
import random as rand
from mysql.connector import Error

initTables = [
    """
    CREATE TABLE Employee(
        employeeName VARCHAR(255) NOT NULL, 
        employeeID INTEGER NOT NULL, 
        employeeSSN INTEGER NOT NULL, 
        hireDate DATE, 
        dateOfBirth DATE, 
        PRIMARY KEY (employeeID)
        )
    """,
    """
    CREATE TABLE Department(
        departmentName VARCHAR(255) NOT NULL, 
        departmentID INTEGER NOT NULL AUTO_INCREMENT, 
        numEmployees INTEGER, 
        PRIMARY KEY (departmentID)
        )
    """,
    """
    CREATE TABLE Client(
        clientName VARCHAR(255) NOT NULL, 
        clientID INTEGER NOT NULL AUTO_INCREMENT, 
        clientOrg VARCHAR(255), 
        clientNumber VARCHAR(255), 
        clientEmail VARCHAR(255), 
        PRIMARY KEY (clientID)
        )
    """,
    """
    CREATE TABLE Project(
        projectTitle VARCHAR(255) NOT NULL, 
        projectID INTEGER NOT NULL AUTO_INCREMENT, 
        projectStatus VARCHAR(255) NOT NULL, 
        deliverByDate DATE, 
        PRIMARY KEY (projectID)
        )
    """,
    """
    CREATE TABLE Shipment(
        shipmentID INTEGER NOT NULL AUTO_INCREMENT, 
        shippingCompany VARCHAR(255), 
        arriveByDate DATE, 
        itemCount INTEGER, 
        deliveryLocation VARCHAR(255) NOT NULL, 
        PRIMARY KEY (shipmentID)
        )
    """,
    """
    CREATE TABLE Cargo(
        itemName VARCHAR(255) NOT NULL, 
        itemQuantity INTEGER, 
        itemID INTEGER NOT NULL AUTO_INCREMENT, 
        clientID INTEGER NOT NULL, 
        projectID INTEGER NOT NULL,
        FOREIGN KEY (clientID) REFERENCES Client(clientID) ON DELETE CASCADE, 
        FOREIGN KEY (projectID) REFERENCES Project(projectID) ON DELETE CASCADE, 
        PRIMARY KEY (itemID)
        )
    """,
    """
    CREATE TABLE Manages(
        employeeID INTEGER NOT NULL,  
        departmentID INTEGER NOT NULL, 
        FOREIGN KEY (employeeID) REFERENCES Employee(employeeID) ON DELETE CASCADE, 
        FOREIGN KEY (departmentID) REFERENCES Department(departmentID) ON DELETE CASCADE
        )
    """,
    """
    CREATE TABLE worksFor(
        employeeID INTEGER NOT NULL, 
        departmentID INTEGER NOT NULL, 
        FOREIGN KEY (employeeID) REFERENCES Employee(employeeID) ON DELETE CASCADE, 
        FOREIGN KEY (departmentID) REFERENCES Department(departmentID) ON DELETE CASCADE
        )
    """,
    """
    CREATE TABLE worksOn(
        departmentID INTEGER NOT NULL, 
        projectID INTEGER NOT NULL,
        FOREIGN KEY (departmentID) REFERENCES Department(departmentID), 
        FOREIGN KEY (projectID) REFERENCES Project(projectID) ON DELETE CASCADE
        )
    """,
    """
    CREATE TABLE Requests(
        clientID INTEGER NOT NULL, 
        projectID INTEGER NOT NULL, 
        FOREIGN KEY (clientID) REFERENCES Client(clientID) ON DELETE CASCADE, 
        FOREIGN KEY (projectID) REFERENCES Project(projectID) ON DELETE CASCADE
        )
    """,
    """
    CREATE TABLE shippedBy(
        shipmentID INTEGER NOT NULL, 
        projectID INTEGER NOT NULL, 
        FOREIGN KEY (shipmentID) REFERENCES Shipment(shipmentID) ON DELETE CASCADE, 
        FOREIGN KEY (projectID) REFERENCES Project(projectID) ON DELETE CASCADE
        )
    """
]
# WORK HORSE FUNCTIONS ------------------------------------------------------------------------------------------------


def connectToDatabase(h='localhost', u='root', p='password', db='freshPrints'):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=h,
            user=u,
            password=p,
            database=db
        )
        print('Connected to ' + db + ' database successfully')
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def executeQuery(connect, query):
    cursor = connect.cursor(buffered=True)
    try:
        cursor.execute(query)
        connect.commit()
        print('Query: ' + query + ' executed successfully')
    except Error as err:
        print(f"Error: '{err}'")


def executeManyQueries(connect, query, values):
    cursor = connect.cursor(buffered=True)
    try:
        cursor.executemany(query, values)
        connect.commit()
        print('The Query: ' + query + ' executed successfully for all values')
    except Error as err:
        print(f"Error: '{err}'")


def readQuery(connect, query):
    cursor = connect.cursor(buffered=True)
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


def readManyQueries(connect, query, values):
    cursor = connect.cursor(buffered=True)
    try:
        cursor.executemany(query, values)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error as '{err}'")


def readSingleQuery(connect, query):
    cursor = connect.cursor(buffered=True)
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    except Error as err:
        print(f"Error: '{err}'")

# ADDITION FUNCTIONS --------------------------------------------------------------------------------------------------


def addDepartment(connect, deptName):
    values = (deptName.strip(), 'NULL')
    sql = '''
        INSERT INTO Department (departmentName, numEmployees) 
        VALUES ('%s', %s)
    ''' % values
    executeQuery(connect, sql)


def addEmployee(connect, empName, empSSN=str(rand.randint(100000000, 999999999)), empHireDate='NULL', empDOB='NULL'):
    values = (empName, empSSN[5:], empSSN, empHireDate, empDOB)
    sql = '''
        INSERT INTO Employee (employeeName, employeeID, employeeSSN, hireDate, dateOfBirth) 
        VALUES ('%s', '%s', '%s', '%s', '%s')
    ''' % values
    executeQuery(connect, sql)


def addClient(connect, cliName, cliOrg='NULL', cliNum='NULL', cliEmail='NULL'):
    values = (cliName, cliOrg, cliNum, cliEmail)
    sql = '''
        INSERT INTO Client (clientName, clientOrg, clientNumber, clientEmail) 
        VALUES ('%s', '%s', '%s', '%s')
    ''' % values
    executeQuery(connect, sql)


def addProject(connect, projTitle, projStatus, projDeliverDate='NULL'):
    values = (projTitle, projStatus, projDeliverDate)
    sql = '''
        INSERT INTO Project (projectTitle, projectStatus, deliverByDate) 
        VALUES ('%s', '%s', '%s')
    ''' % values
    executeQuery(connect, sql)


def addShipment(connect, shipCompany='NULL', shipByDate='NULL', shipItemCount='NULL', shipLocation='NULL'):
    values = (shipCompany, shipByDate, shipItemCount, shipLocation)

    sql = '''
        INSERT INTO Shipment (shippingCompany, arriveByDate, itemCount, deliveryLocation) 
        VALUES ('%s', '%s', %s, '%s')
    ''' % values
    executeQuery(connect, sql)


def addCargo(connect, itemName, clientID, itemQuantity=1):
    values = (itemName, itemQuantity, clientID)
    sql = '''
        INSERT INTO Cargo (itemName, itemQuantity, clientID)
        VALUES ('%s', %s, %s)
    ''' % values
    executeQuery(connect, sql)


def addEmpToDept(connect, empID, deptID):
    sql = '''
        INSERT INTO worksFor (employeeID, departmentID)
        VALUES (%s, %s)
    ''' % (empID, deptID)
    executeQuery(connect, sql)


def createManager(connect, empID, deptID):
    sql = '''
        SELECT employeeID
        FROM Manages
        WHERE employeeID = %s OR departmentID = %s
    ''' % (empID, deptID)

    managerID = readSingleQuery(connect, sql)

    if not managerID:
        sql = '''
            INSERT INTO Manages (employeeID, departmentID)
            VALUES (%s, %s)
        ''' % (empID, deptID)
        executeQuery(connect, sql)
    else:
        print("The department already has a manager or the employee manages another department")

# RETRIEVAL FUNCTIONS -------------------------------------------------------------------------------------------------


def printTable(connect, tableName):
    sql = '''
        SELECT *
        FROM %s
    ''' % tableName
    cursor = connect.cursor(buffered=True)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except Error as err:
        print(f"Error: '{err}'")
        return

    if results:
        widths = []
        columns = []
        vertical = '|'
        horizontal = '+'

        for cd in cursor.description:
            columns.append(cd[0].strip())

        for col in range(len(columns)):  # NEW METHOD MAKES MORE SENSE
            maxWidth = 0
            lengths = []
            for i in range(len(results)):  # Runs through all results in the specific column
                lengths.append(len(str(results[i][col])))  # Adds results to a list of lengths
                if maxWidth < max(len(columns[col]), max(lengths)):  # Compares the length of the column name to the results
                    maxWidth = max(len(columns[col]), max(lengths))
                    
            widths.append(maxWidth)
                
        '''for r in range(len(results[0])):  OLD METHOD
            maxWidth = 0
            lengths = []
            for i in results:
                lengths.append(len(str(i[r])))

            for col in columns:
                print(maxWidth)
                print(len(col))
                print(max(lengths))
                if maxWidth < max(len(col), max(lengths)):
                    maxWidth = max(len(col), max(lengths))
                
            widths.append(maxWidth)'''

        for w in widths:
            vertical += " %-" + "%ss |" % (w,)
            horizontal += '-' * w + '--+'

        print(horizontal)
        print(vertical % tuple(columns))
        print(horizontal)
        for row in results:
            print(vertical % row)
        print(horizontal)
    else:
        print(tableName + " table is empty")


def getProjectStatus(connect, projID):
    sql = '''
        SELECT projectStatus
        FROM Project
        Where projectID = %s
    ''' % projID

    result = readSingleQuery(connect, sql)
    result = result[0]

    return result


def empInDept(connect, managerID):
    sql = '''
        SELECT departmentID
        FROM Manages
        WHERE employeeID = %s
    ''' % managerID
    deptID = readQuery(connect, sql)

    sql = '''
        SELECT employeeID
        FROM worksFor
        WHERE departmentID = %s
    ''' % str(deptID[0][0])

    empIDs = readQuery(connect, sql)

    for ID in empIDs:
        sql = '''
                SELECT employeeName, employeeID
                FROM employee
                WHERE employeeID = %s
            ''' % ID[0]
        print(readSingleQuery(connect, sql))


def getActiveProjects(connect, deptID):
    activeProjects = []
    sql = '''
        SELECT projectID
        FROM worksOn
        WHERE departmentID = %s
    ''' % deptID

    projects = readQuery(connect, sql)

    for project in projects:
        sql = '''
            SELECT projectStatus
            FROM Project
            WHERE projectID = %s
        ''' % project[0]

        status = readSingleQuery(connect, sql)

        if int(status[0].strip('%')) > 0:
            activeProjects.append(project[0])

    for project in activeProjects:
        sql = '''
                SELECT projectTitle, projectID, projectStatus
                FROM Project
                WHERE projectID = %s
            ''' % project
        print(readSingleQuery(connect, sql))


def findManager(connect, deptID):
    sql = '''
        SELECT employeeID
        FROM Manages
        WHERE departmentID = %s
    ''' % deptID
    managerID = readSingleQuery(connect, sql)

    sql = '''
        SELECT departmentName
        FROM Department
        WHERE departmentID = %s
    ''' % deptID
    dept = readSingleQuery(connect, sql)

    if managerID:
        sql = '''
            SELECT employeeName
            FROM Employee
            WHERE employeeID = %s
        ''' % managerID
        print(str(readSingleQuery(connect, sql)[0]) + " manages the " + str(dept[0]) + " department")
    else:
        print(str(dept[0]) + " department does not have a manager")


def printMainMenu():
    print("Options: to execute an option, type the number + character (1a, 3c, etc) or exit to exit")
    print("0. Connect to the database:")
    print("\ta. Connect to Database")
    print("1. Add something to the database:")
    print("\ta. Add Department")
    print("\tb. Add Employee")
    print("\tc. Add Client")
    print("2. Remove something from database:")
    print("\ta. Remove Department")
    print("\tb. Remove Employee")
    print("\tc. Remove Client")
    print("3. Update entity in database:")
    print("\ta. Update Department")
    print("\tb. Update Employee")
    print("\tc. Update Client")
    print("\td. Update Project")
    print("\te. Update Shipment")
    print("4. Retrieve information from the database:")
    print("\ta. Retrieve all Departments")
    print("\tb. Retrieve all Employees")
    print("\tc. Retrieve all Clients")
    print("\td. Retrieve all Projects")
    print("5. For client:")
    print("\ta. Request a Project to be undertaken")
    print("\tb. Cancel a Project (If the completion is under 30%)")
    print("\tc. Check status of Project")
    print("6. For managers:")
    print("\ta. New manager")
    print("\tb. Remove manager")
    print("\tc. Check employees in manager's department")
    print("\td. Add employee to department")
    print("\te. Remove employee from department")
    print("7. For department")
    print("\ta. Check active projects")
    print("\tb. See who manages department")
    print("\tc. Complete a project")
    print("8. For advanced users")
    print("\ta. Execute a hand-written query")
    print("\tb. Execute a hand-written query then print it")

# DELETE FUNCTIONS VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV


def delEntryFromTable(connect, tableName, delCond):
    sql = '''
        DELETE FROM %s
        WHERE %s
    ''' % (tableName, delCond)
    executeQuery(connect, sql)


def delEmpFromDept(connect, empID):
    delEntryFromTable(connect, 'worksFor', ('employeeID = ' + str(empID)))


def delManager(connect, empID, deptID):
    sql = '''
        SELECT employeeID
        FROM Manages
        WHERE employeeID = %s
    ''' % empID
    result = readSingleQuery(connect, sql)
    if result:
        sql = '''
            SELECT departmentID
            FROM Manages
            WHERE departmentID = %s
        ''' % deptID
        result = readSingleQuery(connect, sql)
        if result:
            delEntryFromTable(connect, 'Manages', ('employeeID = ' + str(empID) + ' AND  departmentID = ' + str(deptID)))
        else:
            print("The manager with ID: " + str(empID) + " doesn't manage the given department")
    else:
        print("There is no manager with ID: " + str(empID))


def cancelProject(connect, projID, clientID):
    projStatus = getProjectStatus(connect, projID)
    sql = '''
        SELECT *
        FROM Requests
        WHERE clientID = %s
    ''' % clientID
    print(readSingleQuery(connect, sql))
    if readSingleQuery(connect, sql):
        if int(projStatus.strip('%')) <= 30:
            delEntryFromTable(connect, 'Project', ('projectID = ' + str(projID)))
        else:
            print("Project is too far into production cannot be canceled")
    else:
        print("This client did not request the project being deleted")

# FUNCTIONS -----------------------------------------------------------------------------------------------------------


def completeProject(connect, deptID, projID):
    projStatus = getProjectStatus(connect, projID)
    sql = '''
        SELECT projectID
        FROM worksOn
        WHERE departmentID = %s
    ''' % deptID

    dept = readQuery(connect, sql)

    if dept:
        for d in dept:
            if int(d[0]) == projID:
                if projStatus == '100%':
                    delEntryFromTable(connect, 'Project', ('projectID = ' + projID))
                    break
                else:
                    print("The project is not finished yet, cannot complete")
                    break
        else:
            print("This department is not the one working on this project")
    else:
        print("This department has no projects")


def updateEntryFromTable(connect, tableName, updVal, updCond):
    sql = '''
        UPDATE %s
        SET %s
        WHERE %s
    ''' % (tableName, updVal, updCond)
    executeQuery(connect, sql)


def requestProject(connect, clientID):
    title = str(input("Please enter the title of the project: "))
    date = str(input("Please enter the delivery date (YYYY-MM-DD), if one is unspecified leave blank: "))
    if date:
        addProject(connect, title, '0%', date)
    else:
        addProject(connect, title, '0%')

    printTable(connect, 'Project')
    prID = int(input("Please enter the ID of the project just created: "))

    sql = '''
            INSERT INTO Requests (clientID, projectID)
            VALUES (%s, %s)
        ''' % (clientID, prID)
    executeQuery(connect, sql)

    company = str(input("Please enter the name of the company delivering the project: "))
    location = str(input("Please enter the location the project should be delivered to: "))
    itemCount = int(input("Please enter the number of UNIQUE items you are ordering: "))
    addShipment(connect, company, date, str(itemCount), location)
    printTable(connect, 'Shipment')
    shipID = int(input("please enter the ID of the shipment just created: "))

    sql = '''
        INSERT INTO shippedBy (shipmentID, projectID)
        VALUES (%s, %s)
    ''' % (shipID, prID)
    executeQuery(connect, sql)

    for i in range(itemCount):
        itemName = str(input("Please enter the name of the item: "))
        itemQuantity = int(input("Please enter the quantity of the item: "))
        addCargo(connect, itemName, clientID, itemQuantity)

    sql = '''
        INSERT INTO shippedBy (shippingID, projectID)
        VALUES (%s, %s)
    ''' % (shipID, prID)
    executeQuery(connect, sql)

    printTable(connect, 'Department')
    deptID = int(input("Please enter the ID of the department you want to work on the project: "))

    sql = '''
        INSERT INTO worksOn (departmentID, projectID)
        VALUES (%s, %s)
    ''' % (deptID, prID)
    executeQuery(connect, sql)

# DEV FUNCTIONS -------------------------------------------------------------------------------------------------------


def deleteEveryTable(connect):  # For dev purpose
    executeQuery(connect, 'DROP TABLE worksOn')
    executeQuery(connect, 'DROP TABLE worksFor')
    executeQuery(connect, 'DROP TABLE Requests')
    executeQuery(connect, 'DROP TABLE shippedBy')
    executeQuery(connect, 'DROP TABLE Cargo')
    executeQuery(connect, 'DROP TABLE Manages')
    executeQuery(connect, 'DROP TABLE Employee')
    executeQuery(connect, 'DROP TABLE Client')
    executeQuery(connect, 'DROP TABLE Department')
    executeQuery(connect, 'DROP TABLE Project')
    executeQuery(connect, 'DROP TABLE Shipment')


def createEveryTable(connect, tables):  # For dev purpose
    for i in tables:
        executeQuery(connect, i)


if __name__ == "__main__":  # MAIN ------------------------------------------------------------------------------------
    validInp = [
        '0a', '1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c', '3d',
        '4a', '4b', '4c', '4d', '5a', '5b', '5c', '5d', '6a', '6b', '6c',
        '6d', '6e', '7a', '7b', '7c', '8a', '8b',  'exit']
    connectedToDB = False
    inpString = ''
    while inpString != 'exit':
        if connectedToDB:
            toss = input("Input anything to continue: ")
        printMainMenu()
        inpString = str(input("Please enter your input: "))

        while inpString not in validInp:
            inpString = str(input("Please enter a valid input: "))

        if inpString[0] == '0':  # Connect to the db
            if connectedToDB:
                print("Already connected to the database")
                continue
            password = str(input("Please enter the password to the root user: "))
            mydb = connectToDatabase('localhost', 'root', password, 'freshPrints')
            connectedToDB = True
            continue

        if connectedToDB:
            if inpString[0] == '1':  # Add something to a table
                if inpString[1] == 'a':  # Add department
                    dName = str(input("What would you like the departments name to be: "))
                    addDepartment(mydb, dName)
                elif inpString[1] == 'b':  # Add employee
                    eName = str(input("Please enter the employee's name: "))
                    eSSN = str(input("Please enter the employee's SSN (No hyphens please): "))
                    eDate = str(input("Please enter the employee's join date (YYYY-MM-DD): "))
                    eDOB = str(input("Please enter the employee's date of birth (YYYY-MM-DD): "))
                    addEmployee(mydb, eName, eSSN, eDate, eDOB)
                elif inpString[1] == 'c':  # Add client
                    cName = str(input("Please enter the client's name: "))
                    cOrg = str(input("Please enter the client's organization: "))
                    cNum = str(input("Please enter the client's phone number: "))
                    cEmail = str(input("Please enter the client's email: "))
                    addClient(mydb, cName, cOrg, cNum, cEmail)
                continue

            elif inpString[0] == '2':  # Remove something from a table
                if inpString[1] == 'a':  # Delete department
                    printTable(mydb, 'Department')
                    dID = str(input("Please type the ID of the department you wish to delete: "))
                    delEntryFromTable(mydb, 'Department', ('departmentID = ' + dID))
                    printTable(mydb, 'Department')
                elif inpString[1] == 'b':  # Delete employee
                    printTable(mydb, 'Employee')
                    eID = str(input("Please type the ID of the employee you wish to delete: "))
                    delEntryFromTable(mydb, 'Employee', ('employeeID = ' + eID))
                    printTable(mydb, 'Employee')
                elif inpString[1] == 'c':  # Delete client
                    printTable(mydb, 'Client')
                    cID = str(input("Please type the ID of the client you wish to delete: "))
                    delEntryFromTable(mydb, 'Client', ('clientID = ' + cID))
                    printTable(mydb, 'Client')
                continue

            elif inpString[0] == '3':  # Update entry in table
                if inpString[1] == 'a':  # Update department
                    printTable(mydb, 'Department')
                    dID = str(input("Please enter the ID of the department you wish to update: "))
                    dName = str(input("Please enter the new name for the selected department: "))
                    updateEntryFromTable(mydb, 'Department', ('departmentName = \'' + dName + '\''), ('departmentID = ' + dID))
                    printTable(mydb, 'Department')
                elif inpString[1] == 'b':  # Update employee
                    printTable(mydb, 'Employee')
                    eID = str(input("Please enter the ID of the employee you wish to update: "))
                    eName = str(input("Please enter the new name of the employee you wish to update: "))
                    updateEntryFromTable(mydb, 'Employee', ('employeeName = \'' + eName + '\''), ('employeeID = ' + eID))
                    printTable(mydb, 'Employee')
                elif inpString[1] == 'c':  # Update client
                    printTable(mydb, 'Client')
                    cInp = str(input("What would you like to update? (org, num, email, or name: "))
                    cID = str(input("Please enter the ID of the client you wish to update: "))
                    if cInp == 'org':
                        cOrg = str(input("Please enter the new organization name of the client: "))
                        updateEntryFromTable(mydb, 'Client', ('clientOrg = \'' + cOrg + '\''), ('clientID = ' + cID))
                    elif cInp == 'num':
                        cNum = str(input("Please enter the new phone number of the client: "))
                        updateEntryFromTable(mydb, 'Client', ('clientNum = \'' + cNum + '\''), ('clientID = ' + cID))
                    elif cInp == 'email':
                        cEmail = str(input("Please enter the new email of the client: "))
                        updateEntryFromTable(mydb, 'Client', ('clientEmail = \'' + cEmail + '\''), ('clientID = ' + cID))
                    elif cInp == 'name':
                        cName = str(input("Please enter the new name of the client: "))
                        updateEntryFromTable(mydb, 'Client', ('clientName = \'' + cName + '\''), ('clientID = ' + cID))
                elif inpString[1] == 'd':  # Update project
                    printTable(mydb, 'Project')
                    pID = str(input("Please enter the ID of the project you wish to update: "))
                    pInp = str(input("What would you like to update? (status, title, delivery): "))
                    if pInp == 'status':
                        pStatus = str(input("Please enter a value between 0 and 100 in increments of 10 for the new status: "))
                        updateEntryFromTable(mydb, 'Project', ('projectStatus = \'' + pStatus + '%\''), ('projectID = ' + pID))
                    elif pInp == 'title':
                        pTitle = str(input("Please enter the new title of the project: "))
                        updateEntryFromTable(mydb, 'Project', ('projectTitle = \'' + pTitle + '\''), ('projectID = ' + pID))
                    elif pInp == 'delivery':
                        pDdate = str(input("Please enter the new date (YYYY-MM-DD): "))
                        updateEntryFromTable(mydb, 'Project', ('deliverByDate = \'' + pDdate + '\''), ('projectID = ' + pID))
                elif inpString[1] == 'e':  # Update shipment
                    printTable(mydb, 'Shipment')
                    sID = str(input("Please enter the ID of the ship you wish to update: "))
                    sInp = str(input("What would you like to update? (company, location, arrival): "))
                    if sInp == 'company':
                        sCompany = str(input("Please enter the new companies name: "))
                        updateEntryFromTable(mydb, 'Shipment', ('shippingCompany = \'' + sCompany + '\''), ('shipmentID = ' + sID))
                    elif sInp == 'location':
                        sLocation = str(input("Please enter the new location: "))
                        updateEntryFromTable(mydb, 'Shipment', ('deliveryLocation = \'' + sLocation + '\''), ('shipmentID = ' + sID))
                    elif sInp == 'arrival':
                        sArrival = str(input("Please enter the new arrive by date: "))
                        updateEntryFromTable(mydb, 'Shipment', ('arriveByDate = \'' + sArrival + '\''), ('shipmentID = ' + sID))
                continue

            elif inpString[0] == '4':  # Print tables
                if inpString[1] == 'a':  # Print departments
                    printTable(mydb, 'Department')
                elif inpString[1] == 'b':  # Print employees
                    printTable(mydb, 'Employee')
                elif inpString[1] == 'c':  # Print clients
                    printTable(mydb, 'Client')
                elif inpString[1] == 'd':  # Print projects
                    printTable(mydb, 'Project')
                continue

            elif inpString[0] == '5':  # Client queries
                printTable(mydb, 'Client')
                cID = str(input("Please enter the clients ID: "))
                if inpString[1] == 'a':  # Request a project
                    requestProject(mydb, cID)
                elif inpString[1] == 'b':  # Cancel a project
                    printTable(mydb, 'Project')
                    pID = int(input("Please enter the project ID you wish to remove: "))
                    cancelProject(mydb, pID, cID)
                elif inpString[1] == 'c':  # Check progress of project
                    printTable(mydb, 'Project')
                    pID = int(input("Please enter the project ID you wish to check on: "))
                    print("The project is currently at: " + getProjectStatus(mydb, pID))
                continue

            elif inpString[0] == '6':  # Manager queries
                if inpString[1] == 'a':  # Create manager
                    printTable(mydb, 'Employee')
                    printTable(mydb, 'Department')
                    eID = int(input("Please enter the employee's ID: "))
                    dID = int(input("Please enter the ID of the department: "))
                    createManager(mydb, eID, dID)
                elif inpString[1] == 'b':  # Delete manager
                    printTable(mydb, 'Employee')
                    printTable(mydb, 'Department')
                    eID = int(input("Please enter the employee's ID: "))
                    dID = int(input("Please enter the ID of the department: "))
                    delManager(mydb, eID, dID)
                elif inpString[1] == 'c':  # See employee's manager manages
                    printTable(mydb, 'Manages')
                    mID = int(input("Please enter the ID of the manager: "))
                    empInDept(mydb, mID)
                elif inpString[1] == 'd':  # Add employee to department
                    printTable(mydb, 'Employee')
                    printTable(mydb, 'Department')
                    eID = int(input("Please enter the employee's ID: "))
                    dID = int(input("Please enter the ID of the department: "))
                    addEmpToDept(mydb, eID, dID)
                elif inpString[1] == 'e':  # Remove employee from department
                    printTable(mydb, 'Employee')
                    eID = int(input("Please enter the employee's ID: "))
                    delEmpFromDept(mydb, eID)

            elif inpString[0] == '7':  # For department
                printTable(mydb, 'Department')
                dID = int(input("Please enter the ID of the department: "))
                if inpString[1] == 'a':  # Check active projects
                    getActiveProjects(mydb, dID)
                elif inpString[1] == 'b':  # Who manages department
                    findManager(mydb, dID)
                elif inpString[1] == 'c':  # Complete a project
                    printTable(mydb, 'Project')
                    pID = int(input("Please enter the ID of the project you wish to complete: "))
                    completeProject(mydb, dID, pID)

            elif inpString[0] == '8':  # For advanced users
                if inpString[1] == 'a':  # Execute user specified query
                    q = str(input("Please enter your query, it might be easier to type in notepad first:\n"))
                    executeQuery(mydb, q)
                if inpString[1] == 'b':  # Execute user specified query then print it
                    q = str(input("Please enter your query, it might be easier to type in notepad first:\n"))
                    print(readQuery(mydb, q))

        else:
            if inpString == 'exit':
                break
            print("You must connect to the database in order to work with it")

    if connectedToDB:
        try:
            mydb.disconnect()
        except Error as err:
            print(f"Error: '{err}'")     
        
    print("Goodbye")
