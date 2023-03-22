sap.ui.define([
	"sap/ui/core/mvc/Controller"
], function (Controller) {
	"use strict";
    var pwd;
	return Controller.extend("event.controller.View1", {
	onInit: function() {
		pwd = jQuery.sap.getUriParameters().get("pwd");
			
		var oModel = new sap.ui.model.json.JSONModel("https://multiclone-zsystemsetup.cfapps.eu10.hana.ondemand.com/getevent?event=all");
		this.getView().setModel(oModel);

},
	onPressDetailBack : function() {
			this.getView().byId("splitapp").backDetail();
		},
onRefresh: function(oEvent) {
		this.byId("pullToRefresh").hide();
		pwd = jQuery.sap.getUriParameters().get("pwd");
		var oModel = new sap.ui.model.json.JSONModel("https://multiclone-zsystemsetup.cfapps.eu10.hana.ondemand.com/getevent?event=all");
		this.getView().setModel(oModel);
		this.getView().byId("splitapp").toDetail(this.createId("nodetails"));
		this.getView().byId("splitapp").toMaster(this.createId("master"));
		

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