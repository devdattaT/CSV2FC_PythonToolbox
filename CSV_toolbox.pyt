import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "CSV Toolbox"
        self.alias = "CSV Toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [AppendCSVtoFC, Append_AnyCSVtoFC]


class AppendCSVtoFC(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Append CSV to FeatureClass"
        self.description = "Appends the Data in the CSV File to Selected featureClass"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter("in_csv","Input CSV","Input","DEFile","Required")
        param0.filter.list = ['csv']
        
        param1 = arcpy.Parameter("Featureclass","Featureclass","Input", "DEFeatureClass","Required")
        
        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        import csv
        input_csv_path=parameters[0].valueAsText
        fc_path=parameters[1].valueAsText
        #open a Search Cursor on this featureClass
        cursor=arcpy.da.InsertCursor(fc_path, ['Name', 'SHAPE@Y', 'SHAPE@X'])
        
        with open(input_csv_path, 'rb') as csv_file:
            reader=csv.reader(csv_file)
            for row in reader:
                messages.addMessage(row[2])
                input=(row[2], row[0],row[1])
                #Insert into Cursor
                cursor.insertRow(input)
        del cursor
        messages.addMessage("Finished")
        
        return
        
class Append_AnyCSVtoFC(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Append Any CSV"
        self.description = "Appends Data from any Arbitrary CSV File to Selected featureClass"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter("in_csv","Input CSV","Input","DEFile","Required")
        param0.filter.list = ['csv']
        
        param1 = arcpy.Parameter("XField","X Field","Input","GPString","Required")
        
        param2 = arcpy.Parameter("YField","Y Field","Input","GPString","Required")
        
        param3 = arcpy.Parameter("Name_Field","Name Field","Input","GPString","Required")
        
        param4 = arcpy.Parameter("Featureclass","Featureclass","Input", "DEFeatureClass","Required")
        
        params = [param0, param1, param2, param3, param4]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        #read the First Row in the CSV file
        with open(parameters[0].valueAsText, 'rb') as f:
            first_line = f.readline()
            #split the line
            split=first_line.split(',')
            #Add in the dropDown for XField
            parameters[1].filter.list =split
            #Add in the dropDown for Y Field
            parameters[2].filter.list =split
            #Add in the dropDown for Name Field
            parameters[3].filter.list =split
                
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        import csv
        input_csv_path=parameters[0].valueAsText
        fc_path=parameters[1].valueAsText
        #open a Search Cursor on this featureClass
        cursor=arcpy.da.InsertCursor(fc_path, ['Name', 'SHAPE@Y', 'SHAPE@X'])
        
        with open(input_csv_path, 'rb') as csv_file:
            reader=csv.reader(csv_file)
            for row in reader:
                messages.addMessage(row[2])
                input=(row[2], row[0],row[1])
                #Insert into Cursor
                cursor.insertRow(input)
        del cursor
        messages.addMessage("Finished")
        
        return