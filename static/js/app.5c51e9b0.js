(function(e){function t(t){for(var n,r,a=t[0],l=t[1],c=t[2],d=0,h=[];d<a.length;d++)r=a[d],s[r]&&h.push(s[r][0]),s[r]=0;for(n in l)Object.prototype.hasOwnProperty.call(l,n)&&(e[n]=l[n]);u&&u(t);while(h.length)h.shift()();return i.push.apply(i,c||[]),o()}function o(){for(var e,t=0;t<i.length;t++){for(var o=i[t],n=!0,a=1;a<o.length;a++){var l=o[a];0!==s[l]&&(n=!1)}n&&(i.splice(t--,1),e=r(r.s=o[0]))}return e}var n={},s={app:0},i=[];function r(t){if(n[t])return n[t].exports;var o=n[t]={i:t,l:!1,exports:{}};return e[t].call(o.exports,o,o.exports,r),o.l=!0,o.exports}r.m=e,r.c=n,r.d=function(e,t,o){r.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:o})},r.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.t=function(e,t){if(1&t&&(e=r(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var o=Object.create(null);if(r.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)r.d(o,n,function(t){return e[t]}.bind(null,n));return o},r.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return r.d(t,"a",t),t},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.p="/";var a=window["webpackJsonp"]=window["webpackJsonp"]||[],l=a.push.bind(a);a.push=t,a=a.slice();for(var c=0;c<a.length;c++)t(a[c]);var u=l;i.push([0,"chunk-vendors"]),o()})({0:function(e,t,o){e.exports=o("56d7")},"034f":function(e,t,o){"use strict";var n=o("f198"),s=o.n(n);s.a},1:function(e,t){},2:function(e,t){},3:function(e,t){},4:function(e,t){},5:function(e,t){},"56d7":function(e,t,o){"use strict";o.r(t);var n=o("2b0e"),s=function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",{attrs:{id:"app"}},[o("TVChartContainer"),o("ExchangeList")],1)},i=[],r=function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",{staticClass:"TV"},[o("div",{staticClass:"TVChartContainer",attrs:{id:e.containerId}}),o("p",{on:{click:e.google}},[e._v("BTC-MTL")]),o("p",{on:{click:e.apple}},[e._v("AAPL")]),o("p",{on:{click:e.microsoft}},[e._v("BITTREX:USDT-BTC:BITTREX")])])},a=[],l=o("52b3").defaults({json:!0});const c="http://viradash.herokuapp.com",u={};var d={history:u,getBars:function(e,t,o,n,s,i){var r=e.name.split(/[:\/]/);const a="/data/histoday",d={e:r[0],fsym:r[1],tsym:r[2],toTs:n||"",limit:i||2e3};return l({url:`${c}${a}`,qs:d}).then(t=>{if(console.log({data:t}),t.Response&&"Error"===t.Response)return console.log("CryptoCompare API error:",t.Message),[];if(t.Data.length){console.log(`Actually returned: ${new Date(1e3*t.TimeFrom).toISOString()} - ${new Date(1e3*t.TimeTo).toISOString()}`);var o=t.Data.map(e=>{return{time:1e3*e.time,low:e.low,high:e.high,open:e.open,close:e.close,volume:e.volumefrom}});if(s){var n=o[o.length-1];u[e.name]={lastBar:n}}return o}return[]})}};const h=["1","3","5","15","30","60","120","240","D"],p={supported_resolutions:h};var _={onReady:e=>{console.log("=====onReady running"),setTimeout(()=>e(p),0)},searchSymbols:(e,t,o,n)=>{console.log("====Search Symbols running")},resolveSymbol:(e,t,o)=>{console.log("======resolveSymbol running");var n=e.split(/[:\/]/),s={name:e,description:"",type:"crypto",session:"24x7",timezone:"Etc/UTC",ticker:e,exchange:n[0],minmov:1,pricescale:1e8,has_intraday:!0,intraday_multipliers:["1","60"],supported_resolution:h,volume_precision:8,data_status:"streaming"};n[2].match(/USD|EUR|JPY|AUD|GBP|KRW|CNY/)&&(s.pricescale=100),setTimeout(function(){t(s),console.log("Resolving that symbol....",s)},0)},getBars:function(e,t,o,n,s,i,r){console.log("=====getBars running"),d.getBars(e,t,o,n,r).then(e=>{e.length?s(e,{noData:!1}):s(e,{noData:!0})}).catch(e=>{console.log({err:e}),i(e)})},subscribeBars:(e,t,o,n,s)=>{console.log("=====subscribeBars runnning")},unsubscribeBars:e=>{console.log("=====unsubscribeBars running")},calculateHistoryDepth:(e,t,o)=>{return console.log("=====calculateHistoryDepth running"),e<60?{resolutionBack:"D",intervalBack:"1"}:void 0},getMarks:(e,t,o,n,s)=>{console.log("=====getMarks running")},getTimeScaleMarks:(e,t,o,n,s)=>{console.log("=====getTimeScaleMarks running")},getServerTime:e=>{console.log("=====getServerTime running")}},g=o("ddea");const m=new n["a"];var f=m;function v(){const e=new RegExp("[\\?&]lang=([^&#]*)"),t=e.exec(window.location.search);return null===t?null:decodeURIComponent(t[1].replace(/\+/g," "))}var b={name:"TVChartContainer",data:function(){return{symbol:"Bittrex:ETH/PAY"}},props:{interval:{default:"D",type:String},containerId:{default:"tv_chart_container",type:String},datafeedUrl:{default:"/api",type:String},libraryPath:{default:"/static/charting_library/",type:String},chartsStorageUrl:{default:"https://saveload.tradingview.com",type:String},chartsStorageApiVersion:{default:"1.1",type:String},clientId:{default:"tradingview.com",type:String},userId:{default:"public_user_id",type:String},fullscreen:{default:!1,type:Boolean},autosize:{default:!0,type:Boolean},studiesOverrides:{type:Object,"volume.volume.color.0":"#fe4761","volume.volume.color.1":"#3fcfb4","volume.volume.transparency":10}},methods:{changePair:function(){this.tvWidget&&(this.tvWidget.activeChart().resetData(),this.tvWidget.activeChart().setSymbol(this.symbol))},changeGoogle:function(){this.tvWidget.activeChart().resetData(),this.tvWidget.activeChart().setSymbol("BTC-MTL:BITTREX")},google:function(){this.symbol="Bittrex:BTC/FUN",this.changeGoogle()},microsoft:function(){this.symbol="Bittrex:USD/BTC",this.changePair()},apple:function(){this.symbol="AAPL",this.changePair()}},tvWidget:null,mounted(){let e=this;f.$on("symbol_emitted",function(t){e.symbol=t,e.changePair()});const t={symbol:this.symbol,debug:!1,datafeed:_,interval:this.interval,container_id:this.containerId,library_path:this.libraryPath,toolbar_bg:"#f4f7f9",allow_symbol_change:!0,theme:"Light",locale:v()||"en",disabled_features:["header_symbol_search","header_interval_dialog_button","show_interval_dialog_on_key_press","symbol_search_hot_key","study_dialog_search_control","display_market_status","header_compare","edit_buttons_in_legend","symbol_info","border_around_the_chart","main_series_scale_menu","star_some_intervals_by_default","datasource_copypaste","right_bar_stays_on_scroll","context_menus","go_to_date","compare_symbol","border_around_the_chart","timezone_menu","remove_library_container_border","use_localstorage_for_settings"],enabled_features:["study_templates","dont_show_boolean_study_arguments","use_localstorage_for_settings","remove_library_container_border","save_chart_properties_to_local_storage","side_toolbar_in_fullscreen_mode","hide_last_na_study_output","constraint_dialogs_movement"],charts_storage_url:this.chartsStorageUrl,charts_storage_api_version:this.chartsStorageApiVersion,client_id:this.clientId,user_id:this.userId,fullscreen:this.fullscreen,width:"600",height:"400",autosize:this.autosize},o=new g["widget"](t);this.tvWidget=o,o.onChartReady(()=>{const e=o.createButton().attr("title","Click to show a notification popup").addClass("apply-common-tooltip").on("click",()=>o.showNoticeDialog({title:"Notification",body:"TradingView Charting Library API works correctly",callback:()=>{console.log("Noticed!")}}));e[0].innerHTML="Check API"})},destroyed(){null!==this.tvWidget&&(this.tvWidget.remove(),this.tvWidget=null)}},y=b,w=(o("5c1d"),o("2877")),C=Object(w["a"])(y,r,a,!1,null,"622fbf22",null),S=C.exports,I=function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",{staticClass:"exchangelistcontainer"},[e.exchanges?o("ul",{staticClass:"exchange-name-list"},e._l(e.exchanges,function(t){return o("li",{key:t.id,on:{click:function(o){return e.show_single(t)}}},[e._v("\r\n        "+e._s(t.name)+"\r\n\r\n      ")])}),0):e._e(),e.active_exchange?o("ul",{staticClass:"pair-name-list"},e._l(e.active_exchange.pairs,function(t){return o("li",{key:t.id,on:{click:function(o){return e.show_chart(t)}}},[e._v("\r\n        "+e._s(t)+"\r\n \r\n        \r\n\r\n      ")])}),0):e._e()])},P=[],k={data:function(){return{active_exchange:"",exchanges:[],pair:""}},created(){let e="/api/exchanges";this.$http.get(e).then(e=>{this.exchanges=e.data["exchanges"]}).catch(e=>{console.log(e)})},methods:{show_single(e){this.active_exchange=e},show_chart(e){let t=this.active_exchange.name+":"+e.split("-")[0]+"/"+e.split("-")[1];f.$emit("symbol_emitted",t),this.pair=t}}},A=k,T=(o("e4a2"),Object(w["a"])(A,I,P,!1,null,null,null)),x=T.exports,M={name:"app",components:{ExchangeList:x,TVChartContainer:S}},j=M,R=(o("034f"),Object(w["a"])(j,s,i,!1,null,null,null)),B=R.exports,D=o("2f62"),L=o("bc3a"),U=o.n(L),O=o("a78e"),W=o.n(O),F=U.a.create({baseURL:"/api",timeout:5e3,headers:{"Content-Type":"application/json","X-CSRFToken":W.a.get("csrftoken")}}),E={fetchMessages(){return F.get("messages/").then(e=>e.data)},postMessage(e){return F.post("messages/",e).then(e=>e.data)},deleteMessage(e){return F.delete(`messages/${e}`).then(e=>e.data)},getBTC(){return F.get("bittrex/").then(e=>e.data)}};const z={messages:[],bitcoin:[]},N={bitcoin:e=>{return e.bitcoin},messages:e=>{return e.messages}},$={getMessages({commit:e}){E.fetchMessages().then(t=>{e("setMessages",t)})},getbitcoin({commit:e}){E.getBTC().then(t=>{e("setBitcoin",t)})},addMessage({commit:e},t){E.postMessage(t).then(()=>{e("addMessage",t)})},deleteMessage({commit:e},t){E.deleteMessage(t),e("deleteMessage",t)}},H={setMessages(e,t){e.messages=t},setBitcoin(e,t){e.bitcoin=t},addMessage(e,t){e.messages.push(t)},deleteMessage(e,t){e.messages=e.messages.filter(e=>e.pk!==t)}};var V={namespaced:!0,state:z,getters:N,actions:$,mutations:H};const J={messages:[],bitcoin:[]},q={bitcoin:e=>{return e.bitcoin},messages:e=>{return e.messages}},G={getMessages({commit:e}){E.fetchMessages().then(t=>{e("setMessages",t)})},getbitcoin({commit:e}){E.getBTC().then(t=>{e("setBitcoin",t)})},addMessage({commit:e},t){E.postMessage(t).then(()=>{e("addMessage",t)})},deleteMessage({commit:e},t){E.deleteMessage(t),e("deleteMessage",t)}},X={setMessages(e,t){e.messages=t},setBitcoin(e,t){e.bitcoin=t},addMessage(e,t){e.messages.push(t)},deleteMessage(e,t){e.messages=e.messages.filter(e=>e.pk!==t)}};var Y={namespaced:!0,state:J,getters:q,actions:G,mutations:X};n["a"].use(D["a"]);var K=new D["a"].Store({modules:{messages:V,exch:Y}}),Q=o("8c4f"),Z=function(){var e=this,t=e.$createElement;e._self._c;return e._m(0)},ee=[function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"hello"},[n("img",{attrs:{src:o("e669")}}),n("p",[e._v("\n    For guide and recipes on how to configure / customize this project,"),n("br"),e._v("\n    check out the\n    "),n("a",{attrs:{href:"https://cli.vuejs.org",target:"_blank",rel:"noopener"}},[e._v("vue-cli documentation")]),e._v(".\n  ")]),n("h3",[e._v("Installed CLI Plugins")]),n("ul",[n("li",[n("a",{attrs:{href:"https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel",target:"_blank",rel:"noopener"}},[e._v("babel")])]),n("li",[n("a",{attrs:{href:"https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint",target:"_blank",rel:"noopener"}},[e._v("eslint")])])]),n("h3",[e._v("Essential Links")]),n("ul",[n("li",[n("a",{attrs:{href:"https://vuejs.org",target:"_blank",rel:"noopener"}},[e._v("Core Docs")])]),n("li",[n("a",{attrs:{href:"https://forum.vuejs.org",target:"_blank",rel:"noopener"}},[e._v("Forum")])]),n("li",[n("a",{attrs:{href:"https://chat.vuejs.org",target:"_blank",rel:"noopener"}},[e._v("Community Chat")])]),n("li",[n("a",{attrs:{href:"https://twitter.com/vuejs",target:"_blank",rel:"noopener"}},[e._v("Twitter")])]),n("li",[n("a",{attrs:{href:"https://news.vuejs.org",target:"_blank",rel:"noopener"}},[e._v("News")])])]),n("h3",[e._v("Ecosystem")]),n("ul",[n("li",[n("a",{attrs:{href:"https://router.vuejs.org",target:"_blank",rel:"noopener"}},[e._v("vue-router")])]),n("li",[n("a",{attrs:{href:"https://vuex.vuejs.org",target:"_blank",rel:"noopener"}},[e._v("vuex")])]),n("li",[n("a",{attrs:{href:"https://github.com/vuejs/vue-devtools#vue-devtools",target:"_blank",rel:"noopener"}},[e._v("vue-devtools")])]),n("li",[n("a",{attrs:{href:"https://vue-loader.vuejs.org",target:"_blank",rel:"noopener"}},[e._v("vue-loader")])]),n("li",[n("a",{attrs:{href:"https://github.com/vuejs/awesome-vue",target:"_blank",rel:"noopener"}},[e._v("awesome-vue")])])])])}],te={name:"VueDemo",props:{}},oe=te,ne=(o("c19a"),Object(w["a"])(oe,Z,ee,!1,null,"1fef0148",null)),se=(ne.exports,function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"hello"},[n("img",{staticStyle:{width:"250px"},attrs:{src:o("bdfd")}}),n("p",[e._v("The data below is added/removed from the SQLite Database using Django's ORM and Rest Framework.")]),n("br"),n("p",[e._v("Subject")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.subject,expression:"subject"}],attrs:{type:"text",placeholder:"Hello"},domProps:{value:e.subject},on:{input:function(t){t.target.composing||(e.subject=t.target.value)}}}),n("p",[e._v("Message")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.msgBody,expression:"msgBody"}],attrs:{type:"text",placeholder:"From the other side"},domProps:{value:e.msgBody},on:{input:function(t){t.target.composing||(e.msgBody=t.target.value)}}}),n("br"),n("br"),n("input",{attrs:{type:"submit",value:"Add",disabled:!e.subject||!e.msgBody},on:{click:function(t){return e.addMessage({subject:e.subject,body:e.msgBody})}}}),n("hr"),n("h3",[e._v("Messages on Database")]),0===e.messages.length?n("p",[e._v("No Messages")]):e._e(),e._l(e.messages,function(t,o){return n("div",{key:o,staticClass:"msg"},[n("p",{staticClass:"msg-index"},[e._v("["+e._s(o)+"]")]),n("p",{staticClass:"msg-subject",domProps:{innerHTML:e._s(t.subject)}}),n("p",{staticClass:"msg-body",domProps:{innerHTML:e._s(t.body)}}),n("input",{attrs:{type:"submit",value:"Delete"},on:{click:function(o){return e.deleteMessage(t.pk)}}})])})],2)}),ie=[],re={name:"Messages",data(){return{subject:"",msgBody:""}},computed:Object(D["c"])({messages:e=>e.messages.messages,bitcoin:e=>e.messages.bitcoin}),methods:Object(D["b"])("messages",["addMessage","deleteMessage"]),created(){this.$store.dispatch("messages/getMessages"),this.$store.dispatch("messages/getbitcoin")}},ae=re,le=(o("d41e"),Object(w["a"])(ae,se,ie,!1,null,"ea346a72",null)),ce=le.exports;n["a"].use(Q["a"]);var ue=new Q["a"]({routes:[{path:"/",name:"main",component:S},{path:"/messages",name:"messages",component:ce},{path:"/tv",name:"tv",component:S},{path:"/exchanges",name:"exchanges",component:x}]});n["a"].config.productionTip=!1,n["a"].prototype.$http=U.a;const de=new n["a"]({router:ue,store:K,render:e=>e(B)});de.$mount("#app")},"5c1d":function(e,t,o){"use strict";var n=o("8c58"),s=o.n(n);s.a},6451:function(e,t,o){},"68b2":function(e,t,o){},"8c58":function(e,t,o){},bdfd:function(e,t,o){e.exports=o.p+"static/img/logo-django.624de952.png"},c19a:function(e,t,o){"use strict";var n=o("6451"),s=o.n(n);s.a},d41e:function(e,t,o){"use strict";var n=o("db9c"),s=o.n(n);s.a},db9c:function(e,t,o){},ddea:function(e,t,o){!function(e,o){o(t)}(0,function(e){"use strict";var t=Object.assign||function(e){for(var t,o=arguments,n=1,s=arguments.length;n<s;n++)for(var i in t=o[n])Object.prototype.hasOwnProperty.call(t,i)&&(e[i]=t[i]);return e};function o(e,n){var s=t({},e);for(var i in n)"object"!=typeof e[i]||null===e[i]||Array.isArray(e[i])?void 0!==n[i]&&(s[i]=n[i]):s[i]=o(e[i],n[i]);return s}var n={mobile:{disabled_features:["left_toolbar","header_widget","timeframes_toolbar","edit_buttons_in_legend","context_menus","control_bar","border_around_the_chart"],enabled_features:[]}},s={width:800,height:500,symbol:"AA",interval:"D",timezone:"Etc/UTC",container_id:"",library_path:"",locale:"en",widgetbar:{details:!1,watchlist:!1,watchlist_settings:{default_symbols:[]}},overrides:{"mainSeriesProperties.showCountdown":!1},studies_overrides:{},brokerConfig:{configFlags:{}},fullscreen:!1,autosize:!1,disabled_features:[],enabled_features:[],debug:!1,logo:{},time_frames:[{text:"5y",resolution:"W"},{text:"1y",resolution:"W"},{text:"6m",resolution:"120"},{text:"3m",resolution:"60"},{text:"1m",resolution:"30"},{text:"5d",resolution:"5"},{text:"1d",resolution:"1"}],client_id:"0",user_id:"0",charts_storage_api_version:"1.0",favorites:{intervals:[],chartTypes:[]}};function i(){return"1.14 (internal id aaac22e2 @ 2019-04-04 08:31:56.077488)"}var r=function(){function e(e){if(this._id="tradingview_"+(1048576*(1+Math.random())|0).toString(16).substring(1),this._ready=!1,this._readyHandlers=[],this._onWindowResize=this._autoResizeChart.bind(this),!e.datafeed)throw new Error("Datafeed is not defined");if(this._options=o(s,e),e.preset){var t=n[e.preset];t?(void 0!==this._options.disabled_features?this._options.disabled_features=this._options.disabled_features.concat(t.disabled_features):this._options.disabled_features=t.disabled_features,void 0!==this._options.enabled_features?this._options.enabled_features=this._options.enabled_features.concat(t.enabled_features):this._options.enabled_features=t.enabled_features):console.warn("Unknown preset: `"+e.preset+"`")}"Dark"===this._options.theme&&void 0===this._options.loading_screen&&(this._options.loading_screen={backgroundColor:"#131722"}),this._create()}return e.prototype.onChartReady=function(e){this._ready?e.call(this):this._readyHandlers.push(e)},e.prototype.headerReady=function(){var e=this;return this._innerWindowLoaded.then(function(){return e._innerWindow().headerReady()})},e.prototype.onGrayedObjectClicked=function(e){this._innerAPI().onGrayedObjectClicked(e)},e.prototype.onShortcut=function(e,t){this._innerWindow().createShortcutAction(e,t)},e.prototype.subscribe=function(e,t){this._innerAPI().subscribe(e,t)},e.prototype.unsubscribe=function(e,t){this._innerAPI().unsubscribe(e,t)},e.prototype.chart=function(e){return this._innerAPI().chart(e)},e.prototype.setLanguage=function(e){this.remove(),this._options.locale=e,this._create()},e.prototype.setSymbol=function(e,t,o){this._innerAPI().changeSymbol(e,t+"",o)},e.prototype.remove=function(){window.removeEventListener("resize",this._onWindowResize),this._readyHandlers.splice(0,this._readyHandlers.length),delete window[this._id],this._iFrame.parentNode&&this._iFrame.parentNode.removeChild(this._iFrame)},e.prototype.closePopupsAndDialogs=function(){this._innerAPI().closePopupsAndDialogs()},e.prototype.selectLineTool=function(e){this._innerAPI().selectLineTool(e)},e.prototype.selectedLineTool=function(){return this._innerAPI().selectedLineTool()},e.prototype.save=function(e){this._innerAPI().saveChart(e)},e.prototype.load=function(e,t){this._innerAPI().loadChart({json:e,extendedData:t})},e.prototype.getSavedCharts=function(e){this._innerAPI().getSavedCharts(e)},e.prototype.loadChartFromServer=function(e){this._innerAPI().loadChartFromServer(e)},e.prototype.saveChartToServer=function(e,t,o,n){this._innerAPI().saveChartToServer(e,t,o,n)},e.prototype.removeChartFromServer=function(e,t){this._innerAPI().removeChartFromServer(e,t)},e.prototype.onContextMenu=function(e){this._innerAPI().onContextMenu(e)},e.prototype.createButton=function(e){return this._innerWindow().createButton(e)},e.prototype.showNoticeDialog=function(e){this._innerAPI().showNoticeDialog(e)},e.prototype.showConfirmDialog=function(e){this._innerAPI().showConfirmDialog(e)},e.prototype.showLoadChartDialog=function(){this._innerAPI().showLoadChartDialog()},e.prototype.showSaveAsChartDialog=function(){this._innerAPI().showSaveAsChartDialog()},e.prototype.symbolInterval=function(){return this._innerAPI().getSymbolInterval()},e.prototype.mainSeriesPriceFormatter=function(){return this._innerAPI().mainSeriesPriceFormatter()},e.prototype.getIntervals=function(){return this._innerAPI().getIntervals()},e.prototype.getStudiesList=function(){return this._innerAPI().getStudiesList()},e.prototype.addCustomCSSFile=function(e){this._innerWindow().addCustomCSSFile(e)},e.prototype.applyOverrides=function(e){this._options=o(this._options,{overrides:e}),this._innerWindow().applyOverrides(e)},e.prototype.applyStudiesOverrides=function(e){this._innerWindow().applyStudiesOverrides(e)},e.prototype.watchList=function(){return this._innerAPI().watchlist()},e.prototype.activeChart=function(){return this._innerAPI().activeChart()},e.prototype.chartsCount=function(){return this._innerAPI().chartsCount()},e.prototype.layout=function(){return this._innerAPI().layout()},e.prototype.setLayout=function(e){this._innerAPI().setLayout(e)},e.prototype.layoutName=function(){return this._innerAPI().layoutName()},e.prototype.changeTheme=function(e){this._innerWindow().changeTheme(e)},e.prototype.takeScreenshot=function(){this._innerAPI().takeScreenshot()},e.prototype.lockAllDrawingTools=function(){return this._innerAPI().lockAllDrawingTools()},e.prototype.hideAllDrawingTools=function(){return this._innerAPI().hideAllDrawingTools()},e.prototype.undoRedoState=function(){return this._innerAPI().undoRedoState()},e.prototype._innerAPI=function(){return this._innerWindow().tradingViewApi},e.prototype._innerWindow=function(){return this._iFrame.contentWindow},e.prototype._autoResizeChart=function(){this._options.fullscreen&&(this._iFrame.style.height=window.innerHeight+"px")},e.prototype._create=function(){var e=this,t=this._render(),o=document.getElementById(this._options.container_id);if(null===o)throw new Error("There is no such element - #"+this._options.container_id);o.innerHTML=t,this._iFrame=o.querySelector("#"+this._id);var n=this._iFrame;(this._options.autosize||this._options.fullscreen)&&(n.style.width="100%",this._options.fullscreen||(n.style.height="100%")),window.addEventListener("resize",this._onWindowResize),this._onWindowResize(),this._innerWindowLoaded=new Promise(function(e){var t=function(){n.removeEventListener("load",t,!1),e()};n.addEventListener("load",t,!1)}),this._innerWindowLoaded.then(function(){e._innerWindow().widgetReady(function(){e._ready=!0;for(var t=0,o=e._readyHandlers;t<o.length;t++){var n=o[t];try{n.call(e)}catch(e){console.error(e)}}e._innerWindow().initializationFinished()})})},e.prototype._render=function(){var e=window;e[this._id]={datafeed:this._options.datafeed,customFormatters:this._options.customFormatters,brokerFactory:this._options.brokerFactory,overrides:this._options.overrides,studiesOverrides:this._options.studies_overrides,disabledFeatures:this._options.disabled_features,enabledFeatures:this._options.enabled_features,brokerConfig:this._options.brokerConfig,restConfig:this._options.restConfig,favorites:this._options.favorites,logo:this._options.logo,numeric_formatting:this._options.numeric_formatting,rss_news_feed:this._options.rss_news_feed,newsProvider:this._options.news_provider,loadLastChart:this._options.load_last_chart,saveLoadAdapter:this._options.save_load_adapter,loading_screen:this._options.loading_screen,settingsAdapter:this._options.settings_adapter,customIndicatorsUrl:this._options.indicators_file_name},this._options.saved_data&&(e[this._id].chartContent={json:this._options.saved_data});var t=(this._options.library_path||"")+"static/"+this._options.locale+"-tv-chart.aaac22e21df68f2f7bad.html#symbol="+encodeURIComponent(this._options.symbol)+"&interval="+encodeURIComponent(this._options.interval)+(this._options.timeframe?"&timeframe="+encodeURIComponent(this._options.timeframe):"")+(this._options.toolbar_bg?"&toolbarbg="+this._options.toolbar_bg.replace("#",""):"")+(this._options.studies_access?"&studiesAccess="+encodeURIComponent(JSON.stringify(this._options.studies_access)):"")+"&widgetbar="+encodeURIComponent(JSON.stringify(this._options.widgetbar))+(this._options.drawings_access?"&drawingsAccess="+encodeURIComponent(JSON.stringify(this._options.drawings_access)):"")+"&timeFrames="+encodeURIComponent(JSON.stringify(this._options.time_frames))+"&locale="+encodeURIComponent(this._options.locale)+"&uid="+encodeURIComponent(this._id)+"&clientId="+encodeURIComponent(String(this._options.client_id))+"&userId="+encodeURIComponent(String(this._options.user_id))+(this._options.charts_storage_url?"&chartsStorageUrl="+encodeURIComponent(this._options.charts_storage_url):"")+(this._options.charts_storage_api_version?"&chartsStorageVer="+encodeURIComponent(this._options.charts_storage_api_version):"")+(this._options.custom_css_url?"&customCSS="+encodeURIComponent(this._options.custom_css_url):"")+(this._options.auto_save_delay?"&autoSaveDelay="+encodeURIComponent(String(this._options.auto_save_delay)):"")+"&debug="+this._options.debug+(this._options.snapshot_url?"&snapshotUrl="+encodeURIComponent(this._options.snapshot_url):"")+(this._options.timezone?"&timezone="+encodeURIComponent(this._options.timezone):"")+(this._options.study_count_limit?"&studyCountLimit="+encodeURIComponent(String(this._options.study_count_limit)):"")+(this._options.symbol_search_request_delay?"&ssreqdelay="+encodeURIComponent(String(this._options.symbol_search_request_delay)):"")+(this._options.theme?"&theme="+encodeURIComponent(String(this._options.theme)):"");return'<iframe id="'+this._id+'" name="'+this._id+'"  src="'+t+'"'+(this._options.autosize||this._options.fullscreen?"":' width="'+this._options.width+'" height="'+this._options.height+'"')+' frameborder="0" allowTransparency="true" scrolling="no" allowfullscreen style="display:block;"></iframe>'},e}();window.TradingView=window.TradingView||{},window.TradingView.version=i,e.version=i,e.widget=r,Object.defineProperty(e,"__esModule",{value:!0})})},e4a2:function(e,t,o){"use strict";var n=o("68b2"),s=o.n(n);s.a},e669:function(e,t,o){e.exports=o.p+"static/img/logo-vue.82b9c7a5.png"},f198:function(e,t,o){}});
//# sourceMappingURL=app.5c51e9b0.js.map