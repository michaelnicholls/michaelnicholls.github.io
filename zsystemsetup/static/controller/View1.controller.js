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
summary: function(oEvent) {
	window.open("/thisweek");
},
generate: function (oEvent) {
	var fixed = "https://instructortools.appspot.com/ci/index.html";
	var url = oEvent.getSource().data("url");
	window.open(fixed+url);
},
edit: function (oEvent) {
	var fixed = "/getevent?edit&event=";
	var event = oEvent.getSource().data("event");
	window.open(fixed+event);
},
description: function (oEvent) {
	var country = oEvent.getSource().data("country");
	country = new Intl.DisplayNames(['en'], {type: 'region'}).of(country);
	var fixed = "https://training.sap.com/search?filters%5Bcountry%5D%5B"+country+"%5D=on&q=";
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

