(function(e){function t(t){for(var r,n,a=t[0],l=t[1],c=t[2],d=0,u=[];d<a.length;d++)n=a[d],i[n]&&u.push(i[n][0]),i[n]=0;for(r in l)Object.prototype.hasOwnProperty.call(l,r)&&(e[r]=l[r]);p&&p(t);while(u.length)u.shift()();return s.push.apply(s,c||[]),o()}function o(){for(var e,t=0;t<s.length;t++){for(var o=s[t],r=!0,a=1;a<o.length;a++){var l=o[a];0!==i[l]&&(r=!1)}r&&(s.splice(t--,1),e=n(n.s=o[0]))}return e}var r={},i={app:0},s=[];function n(t){if(r[t])return r[t].exports;var o=r[t]={i:t,l:!1,exports:{}};return e[t].call(o.exports,o,o.exports,n),o.l=!0,o.exports}n.m=e,n.c=r,n.d=function(e,t,o){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:o})},n.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var o=Object.create(null);if(n.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)n.d(o,r,function(t){return e[t]}.bind(null,r));return o},n.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="/";var a=window["webpackJsonp"]=window["webpackJsonp"]||[],l=a.push.bind(a);a.push=t,a=a.slice();for(var c=0;c<a.length;c++)t(a[c]);var p=l;s.push([0,"chunk-vendors"]),o()})({0:function(e,t,o){e.exports=o("56d7")},"034f":function(e,t,o){"use strict";var r=o("f198"),i=o.n(r);i.a},"3f64":function(e,t,o){"use strict";var r=o("dce2"),i=o.n(r);i.a},"56d7":function(e,t,o){"use strict";o.r(t);var r=o("2b0e"),i=function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",{attrs:{id:"app"}},[o("h1",[e._v("Django VueJs Template")]),o("div",{attrs:{id:"nav"}},[o("router-link",{attrs:{to:{name:"home"}}},[e._v("Vue")]),e._v(" |\n   "),o("router-link",{attrs:{to:{name:"messages"}}},[e._v("Django Rest")]),e._v(" | \n    "),o("router-link",{attrs:{to:{name:"tv"}}},[e._v("Chart tv")])],1),o("router-view")],1)},s=[],n=(o("034f"),o("2877")),a={},l=Object(n["a"])(a,i,s,!1,null,null,null),c=l.exports,p=o("2f62"),d=o("bc3a"),u=o.n(d),h=o("a78e"),_=o.n(h),m=u.a.create({baseURL:"/api",timeout:5e3,headers:{"Content-Type":"application/json","X-CSRFToken":_.a.get("csrftoken")}}),f={fetchMessages(){return m.get("messages/").then(e=>e.data)},postMessage(e){return m.post("messages/",e).then(e=>e.data)},deleteMessage(e){return m.delete(`messages/${e}`).then(e=>e.data)},getBTC(){return m.get("bittrex/").then(e=>e.data)}};const g={messages:[],bitcoin:[]},y={bitcoin:e=>{return e.bitcoin},messages:e=>{return e.messages}},v={getMessages({commit:e}){f.fetchMessages().then(t=>{e("setMessages",t)})},getbitcoin({commit:e}){f.getBTC().then(t=>{e("setBitcoin",t)})},addMessage({commit:e},t){f.postMessage(t).then(()=>{e("addMessage",t)})},deleteMessage({commit:e},t){f.deleteMessage(t),e("deleteMessage",t)}},b={setMessages(e,t){e.messages=t},setBitcoin(e,t){e.bitcoin=t},addMessage(e,t){e.messages.push(t)},deleteMessage(e,t){e.messages=e.messages.filter(e=>e.pk!==t)}};var S={namespaced:!0,state:g,getters:y,actions:v,mutations:b};r["a"].use(p["a"]);var w=new p["a"].Store({modules:{messages:S}}),P=o("8c4f"),C=function(){var e=this,t=e.$createElement;e._self._c;return e._m(0)},A=[function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"hello"},[r("img",{attrs:{src:o("e669")}}),r("p",[e._v("\n    For guide and recipes on how to configure / customize this project,"),r("br"),e._v("\n    check out the\n    "),r("a",{attrs:{href:"https://cli.vuejs.org",target:"_blank",rel:"noopener"}},[e._v("vue-cli documentation")]),e._v(".\n  ")]),r("h3",[e._v("Installed CLI Plugins")]),r("ul",[r("li",[r("a",{attrs:{href:"https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel",target:"_blank",rel:"noopener"}},[e._v("babel")])]),r("li",[r("a",{attrs:{href:"https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint",target:"_blank",rel:"noopener"}},[e._v("eslint")])])]),r("h3",[e._v("Essential Links")]),r("ul",[r("li",[r("a",{attrs:{href:"https://vuejs.org",target:"_blank",rel:"noopener"}},[e._v("Core Docs")])]),r("li",[r("a",{attrs:{href:"https://forum.vuejs.org",target:"_blank",rel:"noopener"}},[e._v("Forum")])]),r("li",[r("a",{attrs:{href:"https://chat.vuejs.org",target:"_blank",rel:"noopener"}},[e._v("Community Chat")])]),r("li",[r("a",{attrs:{href:"https://twitter.com/vuejs",target:"_blank",rel:"noopener"}},[e._v("Twitter")])]),r("li",[r("a",{attrs:{href:"https://news.vuejs.org",target:"_blank",rel:"noopener"}},[e._v("News")])])]),r("h3",[e._v("Ecosystem")]),r("ul",[r("li",[r("a",{attrs:{href:"https://router.vuejs.org",target:"_blank",rel:"noopener"}},[e._v("vue-router")])]),r("li",[r("a",{attrs:{href:"https://vuex.vuejs.org",target:"_blank",rel:"noopener"}},[e._v("vuex")])]),r("li",[r("a",{attrs:{href:"https://github.com/vuejs/vue-devtools#vue-devtools",target:"_blank",rel:"noopener"}},[e._v("vue-devtools")])]),r("li",[r("a",{attrs:{href:"https://vue-loader.vuejs.org",target:"_blank",rel:"noopener"}},[e._v("vue-loader")])]),r("li",[r("a",{attrs:{href:"https://github.com/vuejs/awesome-vue",target:"_blank",rel:"noopener"}},[e._v("awesome-vue")])])])])}],I={name:"VueDemo",props:{}},k=I,j=(o("c19a"),Object(n["a"])(k,C,A,!1,null,"1fef0148",null)),x=j.exports,D=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"hello"},[r("img",{staticStyle:{width:"250px"},attrs:{src:o("bdfd")}}),r("p",[e._v("The data below is added/removed from the SQLite Database using Django's ORM and Rest Framework.")]),r("br"),r("p",[e._v("Subject")]),r("input",{directives:[{name:"model",rawName:"v-model",value:e.subject,expression:"subject"}],attrs:{type:"text",placeholder:"Hello"},domProps:{value:e.subject},on:{input:function(t){t.target.composing||(e.subject=t.target.value)}}}),r("p",[e._v("Message")]),r("input",{directives:[{name:"model",rawName:"v-model",value:e.msgBody,expression:"msgBody"}],attrs:{type:"text",placeholder:"From the other side"},domProps:{value:e.msgBody},on:{input:function(t){t.target.composing||(e.msgBody=t.target.value)}}}),r("br"),r("br"),r("input",{attrs:{type:"submit",value:"Add",disabled:!e.subject||!e.msgBody},on:{click:function(t){return e.addMessage({subject:e.subject,body:e.msgBody})}}}),r("hr"),r("h3",[e._v("Messages on Database")]),0===e.messages.length?r("p",[e._v("No Messages")]):e._e(),e._l(e.messages,function(t,o){return r("div",{key:o,staticClass:"msg"},[r("p",{staticClass:"msg-index"},[e._v("["+e._s(o)+"]")]),r("p",{staticClass:"msg-subject",domProps:{innerHTML:e._s(t.subject)}}),r("p",{staticClass:"msg-body",domProps:{innerHTML:e._s(t.body)}}),r("input",{attrs:{type:"submit",value:"Delete"},on:{click:function(o){return e.deleteMessage(t.pk)}}})])})],2)},O=[],T={name:"Messages",data(){return{subject:"",msgBody:""}},computed:Object(p["c"])({messages:e=>e.messages.messages,bitcoin:e=>e.messages.bitcoin}),methods:Object(p["b"])("messages",["addMessage","deleteMessage"]),created(){this.$store.dispatch("messages/getMessages"),this.$store.dispatch("messages/getbitcoin")}},R=T,L=(o("d41e"),Object(n["a"])(R,D,O,!1,null,"ea346a72",null)),M=L.exports,U=function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",[o("div",{staticClass:"TVChartContainer",attrs:{id:e.containerId}}),o("p",{on:{click:e.google}},[e._v("GOOG")]),o("p",{on:{click:e.apple}},[e._v("AAPL")]),o("p",{on:{click:e.microsoft}},[e._v("MSFT")])])},F=[],W=o("ddea");function z(){const e=new RegExp("[\\?&]lang=([^&#]*)"),t=e.exec(window.location.search);return null===t?null:decodeURIComponent(t[1].replace(/\+/g," "))}var B={name:"TVChartContainer",props:{symbol:{default:"BTCUSD:BITTREX",type:String},interval:{default:"D",type:String},containerId:{default:"tv_chart_container",type:String},datafeedUrl:{default:"http://localhost:8000/api",type:String},libraryPath:{default:"/static/charting_library/",type:String},chartsStorageUrl:{default:"https://saveload.tradingview.com",type:String},chartsStorageApiVersion:{default:"1.1",type:String},clientId:{default:"tradingview.com",type:String},userId:{default:"public_user_id",type:String},fullscreen:{default:!1,type:Boolean},autosize:{default:!0,type:Boolean},studiesOverrides:{type:Object,"volume.volume.color.0":"#fe4761","volume.volume.color.1":"#3fcfb4","volume.volume.transparency":75}},methods:{changePair:function(){let e=this;this.chart&&this.feed&&(this.feed._fireEvent("pair_change"),this.chart.activeChart().resetData(),this.chart.activeChart().setSymbol(this.symbol,function(){console.log("GOWNO :: proba zmiany",e.currency1,e.currency2)}))},google:function(){alert("got here"),this.symbol="GOOG",this.changePair()},microsoft:function(){this.symbol="MSFT",this.changePair()},apple:function(){this.symbol="AAPL",this.changePair()}},tvWidget:null,mounted(){const e={symbol:this.symbol,datafeed:new window.Datafeeds.UDFCompatibleDatafeed(this.datafeedUrl),interval:this.interval,container_id:this.containerId,library_path:this.libraryPath,locale:z()||"en",disabled_features:["header_symbol_search","header_interval_dialog_button","show_interval_dialog_on_key_press","symbol_search_hot_key","study_dialog_search_control","display_market_status","header_compare","edit_buttons_in_legend","symbol_info","border_around_the_chart","main_series_scale_menu","star_some_intervals_by_default","datasource_copypaste","right_bar_stays_on_scroll","context_menus","go_to_date","compare_symbol","border_around_the_chart","timezone_menu","remove_library_container_border","use_localstorage_for_settings"],enabled_features:["study_templates","dont_show_boolean_study_arguments","use_localstorage_for_settings","remove_library_container_border","save_chart_properties_to_local_storage","side_toolbar_in_fullscreen_mode","hide_last_na_study_output","constraint_dialogs_movement"],charts_storage_url:this.chartsStorageUrl,charts_storage_api_version:this.chartsStorageApiVersion,client_id:this.clientId,user_id:this.userId,fullscreen:this.fullscreen,width:"600",height:"400",autosize:this.autosize,studies_overrides:this.studiesOverrides,overrides:{"symbolWatermarkProperties.color":"rgba(0,0,0, 0)","paneProperties.background":"#20334d","paneProperties.vertGridProperties.color":"#344568","paneProperties.horzGridProperties.color":"#344568","paneProperties.crossHairProperties.color":"#58637a","paneProperties.crossHairProperties.style":2,"mainSeriesProperties.style":9,"mainSeriesProperties.showCountdown":!1,"scalesProperties.showSeriesLastValue":!0,"mainSeriesProperties.visible":!1,"mainSeriesProperties.showPriceLine":!1,"mainSeriesProperties.priceLineWidth":1,"mainSeriesProperties.lockScale":!1,"mainSeriesProperties.minTick":"default","mainSeriesProperties.extendedHours":!1,volumePaneSize:"tiny",editorFontsList:["Lato","Arial","Verdana","Courier New","Times New Roman"],"paneProperties.topMargin":5,"paneProperties.bottomMargin":5,"paneProperties.leftAxisProperties.autoScale":!0,"paneProperties.leftAxisProperties.autoScaleDisabled":!1,"paneProperties.leftAxisProperties.percentage":!1,"paneProperties.leftAxisProperties.percentageDisabled":!1,"paneProperties.leftAxisProperties.log":!1,"paneProperties.leftAxisProperties.logDisabled":!1,"paneProperties.leftAxisProperties.alignLabels":!0,"paneProperties.legendProperties.showStudyTitles":!0,"paneProperties.legendProperties.showStudyValues":!0,"paneProperties.legendProperties.showSeriesTitle":!0,"paneProperties.legendProperties.showSeriesOHLC":!0,"scalesProperties.showLeftScale":!1,"scalesProperties.showRightScale":!0,"scalesProperties.backgroundColor":"#20334d","scalesProperties.lineColor":"#46587b","scalesProperties.textColor":"#8f98ad","scalesProperties.scaleSeriesOnly":!1,"mainSeriesProperties.priceAxisProperties.autoScale":!0,"mainSeriesProperties.priceAxisProperties.autoScaleDisabled":!1,"mainSeriesProperties.priceAxisProperties.percentage":!1,"mainSeriesProperties.priceAxisProperties.percentageDisabled":!1,"mainSeriesProperties.priceAxisProperties.log":!1,"mainSeriesProperties.priceAxisProperties.logDisabled":!1,"mainSeriesProperties.candleStyle.upColor":"#3fcfb4","mainSeriesProperties.candleStyle.downColor":"#fe4761","mainSeriesProperties.candleStyle.drawWick":!0,"mainSeriesProperties.candleStyle.drawBorder":!0,"mainSeriesProperties.candleStyle.borderColor":"#3fcfb4","mainSeriesProperties.candleStyle.borderUpColor":"#3fcfb4","mainSeriesProperties.candleStyle.borderDownColor":"#fe4761","mainSeriesProperties.candleStyle.wickColor":"#737375","mainSeriesProperties.candleStyle.wickUpColor":"#3fcfb4","mainSeriesProperties.candleStyle.wickDownColor":"#fe4761","mainSeriesProperties.candleStyle.barColorsOnPrevClose":!1,"mainSeriesProperties.hollowCandleStyle.upColor":"#3fcfb4","mainSeriesProperties.hollowCandleStyle.downColor":"#fe4761","mainSeriesProperties.hollowCandleStyle.drawWick":!0,"mainSeriesProperties.hollowCandleStyle.drawBorder":!0,"mainSeriesProperties.hollowCandleStyle.borderColor":"#3fcfb4","mainSeriesProperties.hollowCandleStyle.borderUpColor":"#3fcfb4","mainSeriesProperties.hollowCandleStyle.borderDownColor":"#fe4761","mainSeriesProperties.hollowCandleStyle.wickColor":"#737375","mainSeriesProperties.hollowCandleStyle.wickUpColor":"#3fcfb4","mainSeriesProperties.hollowCandleStyle.wickDownColor":"#fe4761","mainSeriesProperties.haStyle.upColor":"#3fcfb4","mainSeriesProperties.haStyle.downColor":"#fe4761","mainSeriesProperties.haStyle.drawWick":!0,"mainSeriesProperties.haStyle.drawBorder":!0,"mainSeriesProperties.haStyle.borderColor":"#3fcfb4","mainSeriesProperties.haStyle.borderUpColor":"#3fcfb4","mainSeriesProperties.haStyle.borderDownColor":"#fe4761","mainSeriesProperties.haStyle.wickColor":"#737375","mainSeriesProperties.haStyle.wickUpColor":"#3fcfb4","mainSeriesProperties.haStyle.wickDownColor":"#fe4761","mainSeriesProperties.haStyle.barColorsOnPrevClose":!1,"mainSeriesProperties.barStyle.upColor":"#3fcfb4","mainSeriesProperties.barStyle.downColor":"#fe4761","mainSeriesProperties.barStyle.barColorsOnPrevClose":!1,"mainSeriesProperties.barStyle.dontDrawOpen":!1,"mainSeriesProperties.lineStyle.color":"#0cbef3","mainSeriesProperties.lineStyle.linestyle":0,"mainSeriesProperties.lineStyle.linewidth":1,"mainSeriesProperties.lineStyle.priceSource":"close","mainSeriesProperties.areaStyle.color1":"#0cbef3","mainSeriesProperties.areaStyle.color2":"#0098c4","mainSeriesProperties.areaStyle.linecolor":"#0cbef3","mainSeriesProperties.areaStyle.linestyle":0,"mainSeriesProperties.areaStyle.linewidth":1,"mainSeriesProperties.areaStyle.priceSource":"close","mainSeriesProperties.areaStyle.transparency":80}},t=new W["widget"](e);this.tvWidget=t,t.onChartReady(()=>{const e=t.createButton().attr("title","Click to show a notification popup").addClass("apply-common-tooltip").on("click",()=>t.showNoticeDialog({title:"Notification",body:"TradingView Charting Library API works correctly",callback:()=>{console.log("Noticed!")}}));e[0].innerHTML="Check API"})},destroyed(){null!==this.tvWidget&&(this.tvWidget.remove(),this.tvWidget=null)}},N=B,E=(o("3f64"),Object(n["a"])(N,U,F,!1,null,"ed7909b6",null)),V=E.exports;r["a"].use(P["a"]);var H=new P["a"]({routes:[{path:"/",name:"home",component:x},{path:"/messages",name:"messages",component:M},{path:"/tv",name:"tv",component:V}]});r["a"].config.productionTip=!1;const G=new r["a"]({router:H,store:w,render:e=>e(c)});G.$mount("#app")},6451:function(e,t,o){},bdfd:function(e,t,o){e.exports=o.p+"static/img/logo-django.624de952.png"},c19a:function(e,t,o){"use strict";var r=o("6451"),i=o.n(r);i.a},d41e:function(e,t,o){"use strict";var r=o("db9c"),i=o.n(r);i.a},db9c:function(e,t,o){},dce2:function(e,t,o){},ddea:function(e,t,o){!function(e,o){o(t)}(0,function(e){"use strict";var t=Object.assign||function(e){for(var t,o=arguments,r=1,i=arguments.length;r<i;r++)for(var s in t=o[r])Object.prototype.hasOwnProperty.call(t,s)&&(e[s]=t[s]);return e};function o(e,r){var i=t({},e);for(var s in r)"object"!=typeof e[s]||null===e[s]||Array.isArray(e[s])?void 0!==r[s]&&(i[s]=r[s]):i[s]=o(e[s],r[s]);return i}var r={mobile:{disabled_features:["left_toolbar","header_widget","timeframes_toolbar","edit_buttons_in_legend","context_menus","control_bar","border_around_the_chart"],enabled_features:[]}},i={width:800,height:500,symbol:"AA",interval:"D",timezone:"Etc/UTC",container_id:"",library_path:"",locale:"en",widgetbar:{details:!1,watchlist:!1,watchlist_settings:{default_symbols:[]}},overrides:{"mainSeriesProperties.showCountdown":!1},studies_overrides:{},brokerConfig:{configFlags:{}},fullscreen:!1,autosize:!1,disabled_features:[],enabled_features:[],debug:!1,logo:{},time_frames:[{text:"5y",resolution:"W"},{text:"1y",resolution:"W"},{text:"6m",resolution:"120"},{text:"3m",resolution:"60"},{text:"1m",resolution:"30"},{text:"5d",resolution:"5"},{text:"1d",resolution:"1"}],client_id:"0",user_id:"0",charts_storage_api_version:"1.0",favorites:{intervals:[],chartTypes:[]}};function s(){return"1.14 (internal id aaac22e2 @ 2019-04-04 08:31:56.077488)"}var n=function(){function e(e){if(this._id="tradingview_"+(1048576*(1+Math.random())|0).toString(16).substring(1),this._ready=!1,this._readyHandlers=[],this._onWindowResize=this._autoResizeChart.bind(this),!e.datafeed)throw new Error("Datafeed is not defined");if(this._options=o(i,e),e.preset){var t=r[e.preset];t?(void 0!==this._options.disabled_features?this._options.disabled_features=this._options.disabled_features.concat(t.disabled_features):this._options.disabled_features=t.disabled_features,void 0!==this._options.enabled_features?this._options.enabled_features=this._options.enabled_features.concat(t.enabled_features):this._options.enabled_features=t.enabled_features):console.warn("Unknown preset: `"+e.preset+"`")}"Dark"===this._options.theme&&void 0===this._options.loading_screen&&(this._options.loading_screen={backgroundColor:"#131722"}),this._create()}return e.prototype.onChartReady=function(e){this._ready?e.call(this):this._readyHandlers.push(e)},e.prototype.headerReady=function(){var e=this;return this._innerWindowLoaded.then(function(){return e._innerWindow().headerReady()})},e.prototype.onGrayedObjectClicked=function(e){this._innerAPI().onGrayedObjectClicked(e)},e.prototype.onShortcut=function(e,t){this._innerWindow().createShortcutAction(e,t)},e.prototype.subscribe=function(e,t){this._innerAPI().subscribe(e,t)},e.prototype.unsubscribe=function(e,t){this._innerAPI().unsubscribe(e,t)},e.prototype.chart=function(e){return this._innerAPI().chart(e)},e.prototype.setLanguage=function(e){this.remove(),this._options.locale=e,this._create()},e.prototype.setSymbol=function(e,t,o){this._innerAPI().changeSymbol(e,t+"",o)},e.prototype.remove=function(){window.removeEventListener("resize",this._onWindowResize),this._readyHandlers.splice(0,this._readyHandlers.length),delete window[this._id],this._iFrame.parentNode&&this._iFrame.parentNode.removeChild(this._iFrame)},e.prototype.closePopupsAndDialogs=function(){this._innerAPI().closePopupsAndDialogs()},e.prototype.selectLineTool=function(e){this._innerAPI().selectLineTool(e)},e.prototype.selectedLineTool=function(){return this._innerAPI().selectedLineTool()},e.prototype.save=function(e){this._innerAPI().saveChart(e)},e.prototype.load=function(e,t){this._innerAPI().loadChart({json:e,extendedData:t})},e.prototype.getSavedCharts=function(e){this._innerAPI().getSavedCharts(e)},e.prototype.loadChartFromServer=function(e){this._innerAPI().loadChartFromServer(e)},e.prototype.saveChartToServer=function(e,t,o,r){this._innerAPI().saveChartToServer(e,t,o,r)},e.prototype.removeChartFromServer=function(e,t){this._innerAPI().removeChartFromServer(e,t)},e.prototype.onContextMenu=function(e){this._innerAPI().onContextMenu(e)},e.prototype.createButton=function(e){return this._innerWindow().createButton(e)},e.prototype.showNoticeDialog=function(e){this._innerAPI().showNoticeDialog(e)},e.prototype.showConfirmDialog=function(e){this._innerAPI().showConfirmDialog(e)},e.prototype.showLoadChartDialog=function(){this._innerAPI().showLoadChartDialog()},e.prototype.showSaveAsChartDialog=function(){this._innerAPI().showSaveAsChartDialog()},e.prototype.symbolInterval=function(){return this._innerAPI().getSymbolInterval()},e.prototype.mainSeriesPriceFormatter=function(){return this._innerAPI().mainSeriesPriceFormatter()},e.prototype.getIntervals=function(){return this._innerAPI().getIntervals()},e.prototype.getStudiesList=function(){return this._innerAPI().getStudiesList()},e.prototype.addCustomCSSFile=function(e){this._innerWindow().addCustomCSSFile(e)},e.prototype.applyOverrides=function(e){this._options=o(this._options,{overrides:e}),this._innerWindow().applyOverrides(e)},e.prototype.applyStudiesOverrides=function(e){this._innerWindow().applyStudiesOverrides(e)},e.prototype.watchList=function(){return this._innerAPI().watchlist()},e.prototype.activeChart=function(){return this._innerAPI().activeChart()},e.prototype.chartsCount=function(){return this._innerAPI().chartsCount()},e.prototype.layout=function(){return this._innerAPI().layout()},e.prototype.setLayout=function(e){this._innerAPI().setLayout(e)},e.prototype.layoutName=function(){return this._innerAPI().layoutName()},e.prototype.changeTheme=function(e){this._innerWindow().changeTheme(e)},e.prototype.takeScreenshot=function(){this._innerAPI().takeScreenshot()},e.prototype.lockAllDrawingTools=function(){return this._innerAPI().lockAllDrawingTools()},e.prototype.hideAllDrawingTools=function(){return this._innerAPI().hideAllDrawingTools()},e.prototype.undoRedoState=function(){return this._innerAPI().undoRedoState()},e.prototype._innerAPI=function(){return this._innerWindow().tradingViewApi},e.prototype._innerWindow=function(){return this._iFrame.contentWindow},e.prototype._autoResizeChart=function(){this._options.fullscreen&&(this._iFrame.style.height=window.innerHeight+"px")},e.prototype._create=function(){var e=this,t=this._render(),o=document.getElementById(this._options.container_id);if(null===o)throw new Error("There is no such element - #"+this._options.container_id);o.innerHTML=t,this._iFrame=o.querySelector("#"+this._id);var r=this._iFrame;(this._options.autosize||this._options.fullscreen)&&(r.style.width="100%",this._options.fullscreen||(r.style.height="100%")),window.addEventListener("resize",this._onWindowResize),this._onWindowResize(),this._innerWindowLoaded=new Promise(function(e){var t=function(){r.removeEventListener("load",t,!1),e()};r.addEventListener("load",t,!1)}),this._innerWindowLoaded.then(function(){e._innerWindow().widgetReady(function(){e._ready=!0;for(var t=0,o=e._readyHandlers;t<o.length;t++){var r=o[t];try{r.call(e)}catch(e){console.error(e)}}e._innerWindow().initializationFinished()})})},e.prototype._render=function(){var e=window;e[this._id]={datafeed:this._options.datafeed,customFormatters:this._options.customFormatters,brokerFactory:this._options.brokerFactory,overrides:this._options.overrides,studiesOverrides:this._options.studies_overrides,disabledFeatures:this._options.disabled_features,enabledFeatures:this._options.enabled_features,brokerConfig:this._options.brokerConfig,restConfig:this._options.restConfig,favorites:this._options.favorites,logo:this._options.logo,numeric_formatting:this._options.numeric_formatting,rss_news_feed:this._options.rss_news_feed,newsProvider:this._options.news_provider,loadLastChart:this._options.load_last_chart,saveLoadAdapter:this._options.save_load_adapter,loading_screen:this._options.loading_screen,settingsAdapter:this._options.settings_adapter,customIndicatorsUrl:this._options.indicators_file_name},this._options.saved_data&&(e[this._id].chartContent={json:this._options.saved_data});var t=(this._options.library_path||"")+"static/"+this._options.locale+"-tv-chart.aaac22e21df68f2f7bad.html#symbol="+encodeURIComponent(this._options.symbol)+"&interval="+encodeURIComponent(this._options.interval)+(this._options.timeframe?"&timeframe="+encodeURIComponent(this._options.timeframe):"")+(this._options.toolbar_bg?"&toolbarbg="+this._options.toolbar_bg.replace("#",""):"")+(this._options.studies_access?"&studiesAccess="+encodeURIComponent(JSON.stringify(this._options.studies_access)):"")+"&widgetbar="+encodeURIComponent(JSON.stringify(this._options.widgetbar))+(this._options.drawings_access?"&drawingsAccess="+encodeURIComponent(JSON.stringify(this._options.drawings_access)):"")+"&timeFrames="+encodeURIComponent(JSON.stringify(this._options.time_frames))+"&locale="+encodeURIComponent(this._options.locale)+"&uid="+encodeURIComponent(this._id)+"&clientId="+encodeURIComponent(String(this._options.client_id))+"&userId="+encodeURIComponent(String(this._options.user_id))+(this._options.charts_storage_url?"&chartsStorageUrl="+encodeURIComponent(this._options.charts_storage_url):"")+(this._options.charts_storage_api_version?"&chartsStorageVer="+encodeURIComponent(this._options.charts_storage_api_version):"")+(this._options.custom_css_url?"&customCSS="+encodeURIComponent(this._options.custom_css_url):"")+(this._options.auto_save_delay?"&autoSaveDelay="+encodeURIComponent(String(this._options.auto_save_delay)):"")+"&debug="+this._options.debug+(this._options.snapshot_url?"&snapshotUrl="+encodeURIComponent(this._options.snapshot_url):"")+(this._options.timezone?"&timezone="+encodeURIComponent(this._options.timezone):"")+(this._options.study_count_limit?"&studyCountLimit="+encodeURIComponent(String(this._options.study_count_limit)):"")+(this._options.symbol_search_request_delay?"&ssreqdelay="+encodeURIComponent(String(this._options.symbol_search_request_delay)):"")+(this._options.theme?"&theme="+encodeURIComponent(String(this._options.theme)):"");return'<iframe id="'+this._id+'" name="'+this._id+'"  src="'+t+'"'+(this._options.autosize||this._options.fullscreen?"":' width="'+this._options.width+'" height="'+this._options.height+'"')+' frameborder="0" allowTransparency="true" scrolling="no" allowfullscreen style="display:block;"></iframe>'},e}();window.TradingView=window.TradingView||{},window.TradingView.version=s,e.version=s,e.widget=n,Object.defineProperty(e,"__esModule",{value:!0})})},e669:function(e,t,o){e.exports=o.p+"static/img/logo-vue.82b9c7a5.png"},f198:function(e,t,o){}});
//# sourceMappingURL=app.ccbce8bc.js.map