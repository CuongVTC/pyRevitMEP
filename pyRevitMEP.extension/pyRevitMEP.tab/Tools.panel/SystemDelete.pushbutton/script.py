#Code par Cyril Waechter le 14.10.2014
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
getselection = uidoc.Selection.GetElementIds

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import UIApplication
def alert(msg):
   TaskDialog.Show('RevitPythonShell', msg)

def quit():
   __window__.Close()
exit = quit

t = Transaction(doc, "supprimer_syst�me")
t.Start()
#Trouve l'Id des syst�mes des objets s�lectionn�s et supprime ces syst�mes
s = []
for e in getselection():	
	try:
		s.append(doc.GetElement(e).MEPSystem.Id)
	except:
		c = doc.GetElement(e).MEPModel.ConnectorManager.Connectors
		for i in c:
			if i.MEPSystem != None:
				id = Element.Id.GetValue(i.MEPSystem)
				print id
				s.append(id)				
for id in s:
	print id
	doc.Delete(id)
t.Commit()
exit()
	