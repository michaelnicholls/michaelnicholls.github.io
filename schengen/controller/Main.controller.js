sap.ui.define([
	"sap/ui/core/mvc/Controller"
], function (Controller) {
	"use strict";
	var DAYSBEHIND, DAYSAHEAD, FIRSTDATE, MAXDAYS, MAXALLOWED ;

	return Controller.extend("michael.com.schengen.controller.Main", {

	

	onInit: function() {
		var data = {
			minDate: new Date("2021-01-01"),
			maxDate: new Date("2021-12-31"),
			firstDate: new Date(),
			errorFound: false,
			saved: false

		};
		DAYSBEHIND = 180;
		DAYSAHEAD = 365;
		FIRSTDATE = 90;
		MAXDAYS = 180;
		MAXALLOWED = 90;

		var dMin = new Date();
		dMin.setDate(dMin.getDate() - DAYSBEHIND);
		data["minDate"] = dMin;

		var dMax = new Date();
		dMax.setDate(dMax.getDate() + DAYSAHEAD);
		data["maxDate"] = dMax;

		var dFirst = new Date();
		dFirst.setDate(dFirst.getDate() - FIRSTDATE);
		
		var dToday = new Date();
		data["firstDate"] = dToday;

		var event = jQuery.sap.getUriParameters().get("event");
		var oModel = new sap.ui.model.json.JSONModel(data);
		var oStorage = jQuery.sap.storage(jQuery.sap.storage.Type.local);
		var saved = oStorage.get("selected_schengen");
		data["saved"] = (saved != null)  && (saved.length > 2);

		this.getView().setModel(oModel);
		this.getView().byId("calendar").focusDate(dFirst);
		var color = "black";
		for (var i=0;i<DAYSAHEAD;i++) {
		 	var x = new Date();
			x.setDate(x.getDate() + i);
			this.getView().byId("calendar").addSpecialDate(new sap.ui.unified.DateTypeRange({startDate: x, 	color: color, tooltip: "0/"+MAXDAYS}));
			color = "green";
		};
		
		},
		onFirst: function(oEvent) {
		var d = this.getView().getModel().getProperty("/firstDate");
		this.getView().byId("calendar").focusDate(d);
		   
		},
		onClear: function(oEvent) {
			this.getView().byId("calendar").destroySelectedDates();
			this.calculateValidDates();
		},
		onLoad: function(oEvent) {
			var oStorage = jQuery.sap.storage(jQuery.sap.storage.Type.local);
			var saved = oStorage.get("selected_schengen");
			var selected = JSON.parse(saved);
			this.getView().byId("calendar").destroySelectedDates();

			for (var i=0;i<selected.length;i++) {
				var d = new Date(selected[i]);
				this.getView().byId("calendar").addSelectedDate(new sap.ui.unified.DateRange({startDate: d}));				
			};
			this.calculateValidDates();
		},
		onSave: function(oEvent) {
			var arr = [];
			var oCalendar = this.getView().byId("calendar");
			var aSelectedDates = oCalendar.getSelectedDates();
			for (var i = 0;i<aSelectedDates.length;i++) {
				arr.push(aSelectedDates[i].getStartDate());
			};
			var s = JSON.stringify(arr);
			var oStorage = jQuery.sap.storage(jQuery.sap.storage.Type.local);
			oStorage.put("selected_schengen",s);
			var msg = this.getView().getModel("i18n").getResourceBundle().getText("saved");
			sap.m.MessageToast.show(msg);
			this.getView().getModel().setProperty("/saved",true);
		},
		onSelect: function(oEvent) {
			
			this.calculateValidDates();
		},
		calculateValidDates: function() {
			var aSelectedDates = this.getView().byId("calendar").getSelectedDates();
			this.getView().byId("calendar").destroyDisabledDates();
			this.getView().byId("calendar").destroySpecialDates();
			var firstDate = null;
			var errorFound = false;
			for (var i=0;i<365;i++) {
			 	var check = new Date();
				var from = new Date();
         		 	check.setDate(check.getDate() + i);
				from.setDate(from.getDate() + i - MAXDAYS);
				var counter = 0;
				for (var j=0;j<aSelectedDates.length;j++) {
					if (aSelectedDates[j].getStartDate() >= from  && aSelectedDates[j].getStartDate() <= check) {
						counter++; 
					};
				};
				
				if (counter > MAXALLOWED) {
//					this.getView().byId("calendar").addDisabledDate(new sap.ui.unified.DateRange({startDate: check}));
					this.getView().byId("calendar").removeSelectedDate(new sap.ui.unified.DateRange({startDate: check}));
					this.getView().byId("calendar").addSpecialDate(new sap.ui.unified.DateTypeRange({startDate: check, 	color: "red", tooltip: counter+"/"+MAXDAYS}));
					errorFound = true;
				} else {
					var color ="green";
					if (firstDate == null) {
						firstDate = check;
						this.getView().getModel().setProperty("/firstDate",firstDate);
						color = "black";
					};
					this.getView().byId("calendar").addSpecialDate(new sap.ui.unified.DateTypeRange({startDate: check, 	color: color, tooltip: counter+"/"+MAXDAYS}));
				};
				this.getView().getModel().setProperty("/errorFound", errorFound);
			};
			
		},

		/**
		 * Similar to onAfterRendering, but this hook is invoked before the controller's View is re-rendered
		 * (NOT before the first rendering! onInit() is used for that one!).
		 * @memberOf CI.view.ci
		 */
		//	onBeforeRendering: function() {
		//
		//	},

		/**
		 * Called when the View has been rendered (so its HTML is part of the document). Post-rendering manipulations of the HTML could be done here.
		 * This hook is the same one that SAPUI5 controls get after being rendered.
		 * @memberOf CI.view.ci
		 */
		//	onAfterRendering: function() {
		//
		//	},

		/**
		 * Called when the Controller is destroyed. Use this one to free resources and finalize activities.
		 * @memberOf CI.view.ci
		 */
		//	onExit: function() {
		//
		//	}

	});

});