sap.ui.define([
    "sap/ui/core/mvc/Controller"
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (Controller) {
        "use strict";

        return Controller.extend("michael.background.controller.Main", {
            onInit: function () {
                var data = {
                    name: "",
                    course: "",
                    description: "",
                    colours: [
						{"key":"black", "text":"black"},
						{"key":"white", "text":"white"}
						],
                    imageNum: "0",
                    images: [
                        {"id":"0"},
                        {"id":"1"}
                    ],
                    locations: [
                            {"key":"tl", "text":"Top left"},
                            {"key":"tr", "text":"Top right"},
                            {"key":"bl", "text":"Bottom left"},
                            {"key":"br", "text":"Bottom right"}
                            ]
                
        
                };
                var oModel = new sap.ui.model.json.JSONModel(data);
                this.getView().setModel(oModel);
        

            },
            pickImage: function(oEvent) {
                var id = oEvent.getSource().getId();
                var i = id.substr(id.search("--image")+7);
                this.getView().getModel().setProperty("/imageNum",i);
                this.changeImage();
            },
            changeImage: function() {
               var num = this.getView().getModel().getProperty("/imageNum");
               var name = this.getView().getModel().getProperty("/name");
               var course = this.getView().getModel().getProperty("/course");
               var description = this.getView().getModel().getProperty("/description");
               
               var url = "https://sap-netweaver-training.appspot.com/background?i="+num;
               url+="&name="+name;
               url+="&course="+course;
               url+="&description="+description;
               url+="&col="+this.getView().byId("selectColour").getSelectedKey();
               url+="&loc="+this.getView().byId("selectLocation").getSelectedKey();
               this.getView().byId("preview").setSrc(url);

            },
            download: function() {
                var num = this.getView().getModel().getProperty("/imageNum");
                var name = this.getView().getModel().getProperty("/name");
                var course = this.getView().getModel().getProperty("/course");
                var description = this.getView().getModel().getProperty("/description");
                
                var url = "https://sap-netweaver-training.appspot.com/background?i="+num;
                url+="&name="+name;
                url+="&course="+course;
                url+="&description="+description;
                url+="&col="+this.getView().byId("selectColour").getSelectedKey();
                url+="&loc="+this.getView().byId("selectLocation").getSelectedKey();
			    window.open(url);
            }
        });
    });
