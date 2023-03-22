import os
from flask import Flask, request, Response
from cfenv import AppEnv
from hdbcli import dbapi
from datetime import datetime, date
import urllib.request

app = Flask(__name__)
env = AppEnv()

hana_service = 'hana'
hana = env.get_service(label=hana_service)

port = int(os.environ.get('PORT', 3000))
@app.route('/')
def starthere():
    return '<script>window.location.replace("/index.html");</script>'

@app.route('/prompt')
def main():
    html = """
  <form action="/add">
<input name="event" placeholder="event" value="YYYYYYYY">
<input name="course" placeholder="course" value="ABC123">
<input name="instructor" placeholder="instructor" value="Anne Instructor">
<input name="location" placeholder="location" value="Walldorf">
<input name="country" placeholder="country" value="DE">
<input name="lastday" placeholder="lastday" value="YYYY1212">
<input name="groups" placeholder="groups" value="20">
<input name="abappwd" placeholder="abappwd" value="WelcomeYYYY">
<input name="ospwd" placeholder="ospwd" value="SecretYYYY">
<input name="language" placeholder="language" value="E">
<input name="decfmt" placeholder="decfmt" >
<input name="datefmt" placeholder="datefmt">
<input name="clones" placeholder = "clones" value="[st-ut44-999]">

<input type="submit">
</form>  
    """
    return html.replace('YYYY',str(date.today().year))
@app.route('/index.html')
def indexhtml():
     with urllib.request.urlopen("https://multiclone-static.cfapps.eu10.hana.ondemand.com/index.html") as response:
      return response.read()  


@app.route('/index2.html') 
def indexhtml2():
    return """<!DOCTYPE HTML>
<html>

	<head>
		<meta http-equiv="X-UA-Compatible" content="IE=edge" />
		<meta charset="UTF-8">

		<title>SAP Education events based on UT</title>

		<script id="sap-ui-bootstrap"
			src="https://sapui5.hana.ondemand.com/resources/sap-ui-core.js"
			data-sap-ui-libs="sap.m"
			data-sap-ui-theme="sap_belize"
			data-sap-ui-compatVersion="edge"
			data-sap-ui-resourceroots='{"event": ""}'>
		</script>
		<link rel="shortcut icon"  href="/event/favicon.ico"/>
		<link rel="stylesheet" type="text/css" href="css/style.css">

		<script>
/*
var getUrlParameter = function getUrlParameter(sParam) {
		  var sPageURL = window.location.search.substring(1),
        	sURLVariables = sPageURL.split('&'),
        	sParameterName,
        	i;

    	for (i = 0; i < sURLVariables.length; i++) {
        	sParameterName = sURLVariables[i].split('=');

        	if (sParameterName[0] === sParam) {
            	return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        	}
    	}
	};
		var eventNumber = getUrlParameter('event');
		if (typeof eventNumber === "undefined")
*/
			eventNumber = "";

			sap.ui.getCore().attachInit(function() {
				new sap.m.Shell({
					app: new sap.ui.core.ComponentContainer({
						height : "100%",
						name : "event"
					})
				}).placeAt("content");
			});
		</script>
	</head>

	<body class="sapUiBody" id="content">
	</body>

</html>
    """
@app.route('/model/models.js')
def modelsjs2():
   with urllib.request.urlopen("https://multiclone-static.cfapps.eu10.hana.ondemand.com/model/models.js") as response:
      return response.read()  
  

@app.route('/model/models.js2')
def modelsjs():
    return """
    sap.ui.define([
	"sap/ui/model/json/JSONModel",
	"sap/ui/Device"
], function (JSONModel, Device) {
	"use strict";

	return {

		createDeviceModel: function () {
			var oModel = new JSONModel(Device);
			oModel.setDefaultBindingMode("OneWay");
			return oModel;
		}

	};

});
    """
@app.route('/manifest.json')
def manifeset():
   with urllib.request.urlopen("https://multiclone-static.cfapps.eu10.hana.ondemand.com/manifest.json") as response:
      return response.read()  

@app.route('/manifest.json2')
def manifestjson2():
    return """
    {
	"_version": "1.1.0",
	"sap.app": {
		"_version": "1.1.0",
		"id": "event",
		"type": "application",
		"i18n": "i18n/i18n.properties",
		"applicationVersion": {
			"version": "1.0.0"
		},
		"title": "{{appTitle}}",
		"description": "{{appDescription}}",
		"resources": "resources.json",
		"ach": "ach",
		"sourceTemplate": {
			"id": "servicecatalog.connectivityComponent",
			"version": "0.0.0"
		},
		"dataSources": {
			"mainService": {
				"type": "OData",
				"settings": {
					"odataVersion": "2.0",
					"localUri": "localService/metadata.xml"
				},
				"uri": "localService/metadata.xml"
			}
		}
	},
	"sap.ui": {
		"_version": "1.1.0",
		"technology": "UI5",
		"icons": {
			"icon": "",
			"favIcon": "",
			"phone": "",
			"phone@2": "",
			"tablet": "",
			"tablet@2": ""
		},
		"deviceTypes": {
			"desktop": true,
			"tablet": true,
			"phone": true
		},
		"supportedThemes": [
			"sap_hcb",
			"sap_bluecrystal"
		]
	},
	"sap.ui5": {
		"_version": "1.1.0",
		"rootView": {
			"viewName": "event.view.View1",
			"type": "XML"
		},
		"dependencies": {
			"minUI5Version": "1.30.0",
			"libs": {
				"sap.ui.core": {},
				"sap.m": {},
				"sap.ui.layout": {}
			}
		},
		"contentDensities": {
			"compact": true,
			"cozy": true
		},
		"models": {
			"i18n": {
				"type": "sap.ui.model.resource.ResourceModel",
				"settings": {
					"bundleName": "event.i18n.i18n"
				}
			},
			"": {
				"dataSource": "mainService"
			}
		},
		"resources": {
			"css": [
				{
					"uri": "css/style.css"
				}
			]
		},
		"routing": {
			"config": {
				"routerClass": "sap.m.routing.Router",
				"viewType": "XML",
				"async": true,
				"viewPath": "event.view",
				"controlAggregation": "pages",
				"controlId": "idAppControl"
			},
			"routes": [
				{
					"pattern": "Details/{eventId}",
					"name": "Details",
					"target": "Details"
				}
			],
			"targets": {
				"TargetView1": {
					"viewType": "XML",
					"transition": "slide",
					"clearAggregation": true,
					"viewName": "View1"
				},
				"Details": {
					"viewType": "XML",
					"viewName": "Details"
				}
			}
		}
	},
	"sap.platform.hcp": {
		"uri": "webapp",
		"_version": "1.1.0"
	}
}
    """
@app.route('/view/View1.view.xml')
def view():
     with urllib.request.urlopen("https://multiclone-static.cfapps.eu10.hana.ondemand.com/view/View1.view.xml") as response:
      return response.read()  

@app.route('/view/View1.view.xml2')
def view2():
    return """
    <mvc:View xmlns:mvc="sap.ui.core.mvc" controllerName="event.controller.View1" xmlns:l="sap.ui.layout" xmlns:core="sap.ui.core"
	xmlns:html="http://www.w3.org/1999/xhtml" displayBlock="true">
	<App xmlns="sap.m" id="idAppControl">
		<pages>
<!--			<Page title="SAP training event details">
				<content> -->
				<SplitApp id="splitapp" masterButtonText="Events" initialDetail="nodetails">
					<masterPages>
						<Page title="Events ({/Events/length})" id="master">
							<content>
								<PullToRefresh id="pullToRefresh" refresh="onRefresh"/>
								<List items="{/Events}" noDataText="No current events found">
									<items>
										<ObjectListItem type="Navigation" title="{Event/event}" number="{Event/course}({Event/numclones})"
										numberUnit="{Event/location} {Event/country}"
										press="onSelect">
											<firstStatus>
												<ObjectStatus text="UT {Event/ut}"/>
											</firstStatus>
										<ObjectAttribute text="{Event/instructor}"/>
										</ObjectListItem>
											
									</items>
								</List>
							</content>
                            <footer>
                            <Toolbar visible="{/super}">
                            <ToolbarSpacer/>
                            <Button text="Add" press="add" tooltip="Add a new event"/>
                            </Toolbar>
                            </footer>
						</Page>
					</masterPages>
					<detailPages>
						<Page id="nodetails"/>
						<Page id="detailpage" title="Details"  showNavButton="true" navButtonPress="onPressDetailBack">
							<content>
								<l:VerticalLayout  width="100%">
									<l:content>
											<List>
										<DisplayListItem label="Event"	value="{Event/event} (UT {Event/ut})" />
										<DisplayListItem label="Course"	value="{Event/course}" />
										<DisplayListItem label="Instructor"	value="{Event/instructor}" />
										<DisplayListItem label="Country"	value="{Event/country}" />
										<DisplayListItem label="Location"	value="{Event/location}" />
										<DisplayListItem label="Last day"	value="{Event/lastday}" />
<!--										<DisplayListItem label="UT"	value="{Event/ut}" />

										<DisplayListItem label="Groups"	value="{Event/groups}" />
										<DisplayListItem label="ABAP pwd"	value="{Event/abappwd}" />
										<DisplayListItem label="OS pwd"	value="{Event/ospwd}" />
-->
										<DisplayListItem label="Clones ({Event/numclones})"	value="{Event/clones}" />
<!--
										<DisplayListItem label="First setup run at"	value="{Event/firstrun} (UTC)" />
										<DisplayListItem label="Last setup run at"	value="{Event/lastrun} (UTC)" />

										<DisplayListItem label="Language"	value="{Event/language}" />
										<DisplayListItem label="Decimal format"	value="{Event/decfmt}" />
										<DisplayListItem label="Date format"	value="{Event/datefmt}" />
-->									
								</List>
<!--								<l:HorizontalLayout class="sapUiContentPadding" >
										<Link text="Generate connection instructions"
										target="_blank"
							href="https://ci-p2000183813trial.dispatcher.hanatrial.ondemand.com/index.html?ut&amp;instructor={Event/instructor}&amp;course={Event/course}&amp;country={Event/country}&amp;hosts={Event/clones}&amp;event={Event/event}&amp;a={Event/abappwd}&amp;o={Event/ospwd}"/>
								<Text text="Opens in a new window. Please check details before proceeding."/>
								</l:HorizontalLayout> -->
								</l:content>
								</l:VerticalLayout>
							

							</content>
							<footer>
			<OverflowToolbar>
				<ToolbarSpacer/>
				<Button press="description" text="Description" tooltip="Get course description">
					<customData>
				<core:CustomData key="course" value="{Event/course}"/>

					</customData>
				</Button> 

				
				<Button press="generate" text="Generate instructions" tooltip="Generate connection instructions">
					<customData>
						<core:CustomData key="url" value="?ut={Event/ut}&amp;instructor={Event/instructor}&amp;course={Event/course}&amp;country={Event/country}&amp;hosts={Event/clones}&amp;event={Event/event}&amp;a={Event/abappwd}&amp;o={Event/ospwd}"/>


					</customData>
				</Button> 
			</OverflowToolbar>
		</footer>
						</Page>
					</detailPages>
				</SplitApp>
<!--				</content>
			</Page> -->
		</pages>
	</App>
</mvc:View>
    """
@app.route('/controller/View1.controller.js')
def viewcontroller2():
   with urllib.request.urlopen("https://multiclone-static.cfapps.eu10.hana.ondemand.com/controller/View1.controller.js") as response:
      return response.read()  

@app.route('/controller/View1.controller.js2')
def viewcontroller():
    return """
    sap.ui.define([
	"sap/ui/core/mvc/Controller"
], function (Controller) {
	"use strict";
    var pwd;
	return Controller.extend("event.controller.View1", {
	onInit: function() {
        var data = {
            someFlag: false
        };
        var model = new sap.ui.model.json.JSONModel(data);
		pwd = jQuery.sap.getUriParameters().get("pwd");
		var oModel = new sap.ui.model.json.JSONModel("/getevent?event=all&pwd="+pwd);
		this.getView().setModel(oModel);
        this.getView().setModel(model,"extras");
},
	onPressDetailBack : function() {
			this.getView().byId("splitapp").backDetail();
		},
onRefresh: function(oEvent) {
		this.byId("pullToRefresh").hide();
		pwd = jQuery.sap.getUriParameters().get("pwd");
		var oModel = new sap.ui.model.json.JSONModel("/getevent?event=all&pwd="+pwd);
		this.getView().setModel(oModel);
		this.getView().byId("splitapp").toDetail(this.createId("nodetails"));
		this.getView().byId("splitapp").toMaster(this.createId("master"));
		

},
add: function(oEvent) {
    window.open("/prompt");
},
generate: function (oEvent) {
	var fixed = "https://instructortools.appspot.com/ci/index.html";
	var url = oEvent.getSource().data("url");
	window.open(fixed+url);
},
description: function (oEvent) {
	var fixed = "https://training.sap.com/search?q=";
	var course = oEvent.getSource().data("course").split("_")[0];
	window.open(fixed+course);
},
onSelect: function (oEvent) {
			var oItem = oEvent.getSource();
			var oCtx = oItem.getBindingContext();
			var path = oCtx.getPath();
			this.getView().byId("splitapp").to(this.createId("detailpage"));
			this.getView().byId("detailpage").bindElement(path);
		}
	});

});
    """
@app.route('/Component.js')
def componentjs2():
   with urllib.request.urlopen("https://multiclone-static.cfapps.eu10.hana.ondemand.com/Component.js") as response:
      return response.read()  

@app.route('/Component.js2')
def componentJS():
    return """
    sap.ui.define([
	"sap/ui/core/UIComponent",
	"sap/ui/Device",
	"event/model/models"
], function (UIComponent, Device, models) {
	"use strict";

	return UIComponent.extend("event.Component", {

		metadata: {
			manifest: "json"
		},

		/**
		 * The component is initialized by UI5 automatically during the startup of the app and calls the init method once.
		 * @public
		 * @override
		 */
		init: function () {
			// call the base component's init function
			UIComponent.prototype.init.apply(this, arguments);

			// enable routing
			var oRouter = this.getRouter();
			if (oRouter) {
				oRouter.initialize();
			}

			// set the device model
			this.setModel(models.createDeviceModel(), "device");
		}
	});

});
"""
@app.route('/$metadata')
def metadata():
    xml= """<?xml version="1.0" encoding="UTF-8"?>
    <edmx:Edmx xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns:sap="http://www.sap.com/Protocols/SAPData" Version="1.0">
<edmx:DataServices m:DataServiceVersion="2.0">
<Schema xmlns="http://schemas.microsoft.com/ado/2008/09/edm" Namespace="ZEVENT_SRV" xml:lang="en" sap:schema-version="1">
<EntityType Name="EVENT" sap:content-version="1">
<Key>
<PropertyRef Name="event"/>
</Key>
<Property Name="event" Type="Edm.String" Nullable="false" MaxLength="10" sap:unicode="false" sap:creatable="false" sap:updatable="false" sap:sortable="false" sap:filterable="false"/>
<Property Name="instructor" Type="Edm.String" Nullable="false" MaxLength="30" sap:unicode="false" sap:creatable="false" sap:updatable="false" sap:sortable="false" sap:filterable="false"/>
</EntityType>
<EntityContainer Name="ZEVENT_SRV_Entities" m:IsDefaultEntityContainer="true" sap:supported-formats="atom json xlsx">
<EntitySet Name="EVENTSet" EntityType="ZEVENT_SRV.EVENT" sap:creatable="false" sap:updatable="false" sap:deletable="false" sap:pageable="false" sap:addressable="false" sap:content-version="1"/>
</EntityContainer>
<atom:link xmlns:atom="http://www.w3.org/2005/Atom" rel="self" href="http://s4dhost.wdf.sap.corp:8011/sap/opu/odata/SAP/ZEVENT_SRV/$metadata"/>
<atom:link xmlns:atom="http://www.w3.org/2005/Atom" rel="latest-version" href="http://s4dhost.wdf.sap.corp:8011/sap/opu/odata/SAP/ZEVENT_SRV/$metadata"/>
</Schema>
</edmx:DataServices>
</edmx:Edmx>
    """
    return Response(xml,content_type="text/xml")

@app.route('/add')
def add():
    args = request.args
    drop = args.get('drop',default="",type=str)
    if hana is None:
        return "Can't connect to HANA service '{}' – check service name?".format(hana_service)
    else:
        conn = dbapi.connect(address=hana.credentials['host'],
                             port=int(hana.credentials['port']),
                             user=hana.credentials['user'],
                             password=hana.credentials['password'],
                             encrypt='true',
                             sslTrustStore=hana.credentials['certificate'])
        cursor = conn.cursor()
        cursor.execute("select count(*) as c from tables where table_name = 'EVENT' and schema_name = current_schema")
        ro = cursor.fetchone()
        c = str(ro["C"])
        tExists= False
        if ro["C"] == 1:
            tExists = True
        cursor.execute("select count(*) as c from views where view_name = 'EVENT_MASKED' and schema_name = current_schema")
        ro = cursor.fetchone()
        c = str(ro["C"])
        vExists= False
        if ro["C"] == 1:
            vExists = True

        if tExists and drop!="":
            sql = "drop table event cascade"
            cursor.execute(sql)
            tExists = False
        if not tExists:
            sql = "CREATE COLUMN TABLE EVENT(EVENT NVARCHAR(10)"
            sql+=",COURSE NVARCHAR(30)"
            sql+=",INSTRUCTOR NVARCHAR(30)"
            sql+=",LOCATION NVARCHAR(30)"
            sql+=",COUNTRY NVARCHAR(30)"
            sql+=",LASTDAY NVARCHAR(30)"
            sql+=",GROUPS NVARCHAR(30)"
            sql+=",ABAPPWD NVARCHAR(30)"
            sql+=",OSPWD NVARCHAR(30)"
            sql+=",DECFMT NVARCHAR(30)"
            sql+=",DATEFMT NVARCHAR(30)"
            sql+=",LANGUAGE NVARCHAR(30)"
            sql+=",CLONES NVARCHAR(500)"
            sql+=",PRIMARY KEY(EVENT))"
            cursor.execute(sql)
            sql = "grant select on event to dbadmin"
            cursor.execute(sql);
            vExists = False;
        if not vExists:
            sql = "CREATE or replace view EVENT_masked as select "
            sql+="substr(event,1,6)||'**' as event,course,instructor, location,country,lastday,clones from event"
            cursor.execute(sql)
            sql = "grant select,drop on event_masked to dbadmin"
            cursor.execute(sql);
            vExists = False;
        
        event = args.get('event',default="00000000", type=str)
        course = args.get('course',default="None", type=str)
        instructor = args.get('instructor',default="None", type=str).replace("'","''")
        location = args.get('location',default="None", type=str).replace("'","''")
        country = args.get('country',default="None", type=str)
        lastday = args.get('lastday',default="None", type=str)
        groups = args.get('groups',default="None", type=str)
        abappwd = args.get('abappwd',default="None", type=str).replace("'","''")
        ospwd = args.get('ospwd',default="None", type=str).replace("'","''")
        decfmt = args.get('decfmt',default="None", type=str)
        datefmt = args.get('datefmt',default="None", type=str)
        language = args.get('language',default="None", type=str)
        clones = args.get('clones',default="None", type=str)
        
        sql = "upsert event values ('"+event
        sql+= "','"+course
        sql+= "','"+instructor
        sql+= "','"+location
        sql+= "','"+country
        sql+= "','"+lastday
        sql+= "','"+groups
        sql+= "','"+abappwd
        sql+= "','"+ospwd
        sql+= "','"+decfmt
        sql+= "','"+datefmt
        sql+= "','"+language
        sql+= "','"+clones

        sql += "') where event = '"+event+"'" 
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

        return ""

@app.route('/getevent')
def getevent():
    args = request.args
    event = args.get('event',default="",type=str)
    pwd = args.get('pwd',default="",type=str)
    extras = args.get('extras',default="",type=str)
    super = False
    if pwd == "IsEasy":
        super = True
    if hana is None:
        return "Can't connect to HANA service '{}' – check service name?".format(hana_service)
    else:
        conn = dbapi.connect(address=hana.credentials['host'],
                             port=int(hana.credentials['port']),
                             user=hana.credentials['user'],
                             password=hana.credentials['password'],
                             encrypt='true',
                             sslTrustStore=hana.credentials['certificate'])
        cursor = conn.cursor()
        html=""
        now = date.today()
        today = now.strftime("%Y%m%d")
        sql = "delete from event where lastday = 'None' or lastday < '"+today+"'"
        cursor.execute(sql)
        conn.commit()
        table = "event_masked"
        if super:
              table = "event"
        found = False

        if event.isnumeric():
            found = False
            cursor.execute("select * from event where event = '"+event+"'")
            result = cursor.fetchall()
            for row in result:
                found = True
                html+="event:"+row['EVENT']+"\n"
                html+="course:"+row['COURSE']+"\n"
                html+="instructor:"+row['INSTRUCTOR']+"\n"
                html+="location:"+row['LOCATION']+"\n"
                html+="country:"+row['COUNTRY']+"\n"
                html+="lastday:"+row['LASTDAY']+"\n"
                html+="groups:"+row['GROUPS']+"\n"
                html+="abappwd:"+row['ABAPPWD']+"\n"
                html+="ospwd:"+row['OSPWD']+"\n"
                html+="decfmt:"+row['DECFMT']+"\n"
                html+="datefmt:"+row['DATEFMT']+"\n"
                html+="language:"+row['LANGUAGE']+"\n"
                html+="clones:"+row['CLONES']+"\n"
                html+="===================\n"
        elif event=="allhtml":
            counter = 0
            html = """
            <html>
            <head>
            <style>
            a:visited {
            color: blue;
            }
            </style>
            </head>
            <body>
            """
            html+='<table border="1"><tr>'
            cols = "*"
            if extras != "":
                cols+=","+extras
            cursor.execute("select "+cols+" from "+table+" order by event")
            result = cursor.fetchall()
            cols = 0
            pwdcols = []
            datecols = []
            for idx, i in enumerate(cursor.description):
                html+="<th>"+str(i[0]).lower()+"</th>"
                if 'PWD' in str(i[0]):
                    pwdcols.append(idx)
                if 'DAY' in str(i[0]):
                    datecols.append(idx)
                cols=cols+1

            html+="<th>ut</th><th>numclones</th></tr>"
            for row in result:
                found = True
                html+="<tr>"
                numclones = 0
                if '[' in row['CLONES']:
                    numclones = row['CLONES'].count(",") + 1
                ut = "4.x"
                if "ut43" in row["CLONES"].lower():
                    ut = "4.3" 
                if "ut44" in row["CLONES"].lower():
                    ut = "4.4" 
                if "ut45" in row["CLONES"].lower():
                    ut = "4.5" 

                values = range(cols)
                for i in values:
                    if i in pwdcols:
                        html+="<td>***</td>"
                    elif i in datecols:
                        fmtday=row[i]
                        if len(fmtday)==8:
                            fmtday = fmtday[0:4]+"."+fmtday[4:6]+"."+fmtday[6:]
                        html+="<td>"+fmtday+"</td>"    
                    else:
                        html+="<td>"+str(row[i])+"</td>"
                if super: 
                   url = 'https://instructortools.appspot.com/ci/index.html?ut='
                   url+=ut+"&instructor="+row['INSTRUCTOR']
                   url+="&course="+row['COURSE']
                   url+="&country="+row['COUNTRY']
                   url+="&hosts="+row['CLONES']
                   url+="&event="+row['EVENT']
                   url+="&a="+row['ABAPPWD']
                   url+="&o="+row['OSPWD']
      
                html+="<td>"+ut+"</td><td>"+str(numclones)+"</td>"
                if super: 
                    html+='<td><a  href="'+url+'">Connection instructions</a></td>'
                html+='</tr>'
            html+="</table>"
            html+="Number of events: "+  str(len(result))
        else:    
            counter = 0
            found = False
            html+='{"super":'+str(super).lower()+',"Events":['
            cursor.execute("select *,current_schema from "+table+" order by event")
            result = cursor.fetchall()
            field_names = [i[0] for i in cursor.description ]
            for row in result:
                numclones = 0
                if '[' in row['CLONES']:
                    numclones = row['CLONES'].count(",") + 1
                ut = "4.x"
                if "ut43" in row["CLONES"].lower():
                    ut = "4.3" 
                if "ut44" in row["CLONES"].lower():
                    ut = "4.4" 
                if "ut45" in row["CLONES"].lower():
                    ut = "4.5" 
                if counter > 0:
                    html+=","
                counter=counter+1
                lastday=row['LASTDAY']
                if len(lastday)==8:
                    lastday = lastday[0:4]+"."+lastday[4:6]+"."+lastday[6:]
                if super:
                    decfmt = row['DECFMT']
                    datefmt =  row['DATEFMT']
                    if decfmt=="" or decfmt == "1":
                        decfmt="1.234.567,89"
                    if decfmt=="X":
                        decfmt="1,234,567.89"
                    if decfmt=="Y":
                        decfmt="1 234 567,89"
                    if datefmt=="1":
                        datefmt="DD.MM.YYYY"
                    if datefmt=="2":
                        datefmt="MM/DD/YYYY"
                    if datefmt=="3":
                        datefmt="MM-DD-YYYY"
                    if datefmt=="1":
                        datefmt="DD.MM.YYYY"
                    if datefmt=="4":
                        datefmt="YYYY.MM.DD"
                    if datefmt=="5":
                        datefmt="YYYY/MM/DD"
                    if datefmt=="6":
                        datefmt="YYYY-MM-DD"
                    if datefmt=="7":
                        datefmt="GYY.MM.DD (Japanese)"
                    if datefmt=="8":
                        datefmt="GYY/MM/DD (Japanese)"
                    if datefmt=="9":
                        datefmt="GYY-MM-DD (Japanese)"
                    if datefmt=="A":
                        datefmt="YYYY/MM/DD (Islamic 1)"
                    if datefmt=="B":
                        datefmt="YYYY/MM/DD (Islamic 2)"
                    if datefmt=="C":
                        datefmt="YYYY/MM/DD (Iranian)"
                    if datefmt=="":
                        datefmt="unspecified"
               
                found = True
                html+='{"Event":{"event":"'+row['EVENT']+'",'
                html+='"course":"'+row['COURSE']+'",'
                html+='"instructor":"'+row['INSTRUCTOR']+'",'
                html+='"country":"'+row['COUNTRY']+'",'
                html+='"location":"'+row['LOCATION']+'",'
                html+='"lastday":"'+lastday+'",'
                if super:
                    html+='"groups":"'+row['GROUPS']+'",'
                    html+='"abappwd":"'+row['ABAPPWD']+'",'
                    html+='"ospwd":"'+row['OSPWD']+'",'
                    html+='"language":"'+row['LANGUAGE']+'",'
                    html+='"decfmt":"'+decfmt+'",'
                    html+='"datefmt":"'+datefmt+'",'
                html+='"clones":"'+row['CLONES']+'",'
                html+='"numclones":"'+str(numclones)+'",'
                html+='"ut":"'+ut+'",'
                html+='"current_schema":"'+row['CURRENT_SCHEMA']+'",'
                html+='"messageText":"",'
                html+='"messageExists":false,'
                html+='"eventFound":true}}'
 
            html+="]}"
        cursor.close()
        conn.close()
        if not found:
            html = "Invalid event"
        return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
