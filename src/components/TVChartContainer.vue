<template>
  <div>
<div class="TVChartContainer" :id="containerId" />
<p @click="google">GOOG</p>
<p @click="apple">AAPL</p>
<p @click="microsoft">MSFT</p>
</div>
</template>

<script>

import { widget } from '../charting_library.min';

function getLanguageFromURL() {
  const regex = new RegExp('[\\?&]lang=([^&#]*)');
  const results = regex.exec(window.location.search);
  return results === null ? null : decodeURIComponent(results[1].replace(/\+/g, ' '));
}

export default {
  name: 'TVChartContainer',
  props: {
    symbol: {
      default: 'AAPL',
      type: String,
    },
    interval: {
      default: 'D',
      type: String,
    },
    containerId: {
      default: 'tv_chart_container',
      type: String,
    },
    datafeedUrl: {
      default: 'https://demo_feed.tradingview.com',
      type: String,
    },
    libraryPath: {
      default: '/charting_library/',
      type: String,
    },
    chartsStorageUrl: {
      default: 'https://saveload.tradingview.com',
      type: String,
    },
    chartsStorageApiVersion: {
      default: '1.1',
      type: String,
    },
    clientId: {
      default: 'tradingview.com',
      type: String,
    },
    userId: {
      default: 'public_user_id',
      type: String,
    },
    fullscreen: {
      default: false,
      type: Boolean,
    },
    autosize: {
      default: true,
      type: Boolean,
    },
    studiesOverrides: {
      type: Object,
       "volume.volume.color.0": "#fe4761",
                        "volume.volume.color.1": "#3fcfb4",
                        "volume.volume.transparency": 75,
    }
  },
  methods:{
     changePair: function(){
                let this_vue = this;
                if(this.chart && this.feed){
                    this.feed._fireEvent('pair_change');
                    this.chart.activeChart().resetData();
                    this.chart.activeChart().setSymbol(this.symbol, function(){
                        console.log("GOWNO :: proba zmiany",this_vue.currency1,this_vue.currency2);
                    });
                }
            },
    google:function(){
      alert('got here');
      this.symbol='GOOG';
      this.changePair();
    },
    microsoft:function(){
      this.symbol= 'MSFT';
      this.changePair();
    },
    apple:function(){
      this.symbol='AAPL';
      this.changePair();
    }},
  tvWidget: null,
  mounted() {
    const widgetOptions = {
      symbol: this.symbol,
      // BEWARE: no trailing slash is expected in feed URL
      datafeed: new window.Datafeeds.UDFCompatibleDatafeed(this.datafeedUrl),
      interval: this.interval,
      container_id: this.containerId,
      library_path: this.libraryPath,

      locale: getLanguageFromURL() || 'en',
      disabled_features: ["header_symbol_search",
                        "header_interval_dialog_button",
                        "show_interval_dialog_on_key_press",
                        "symbol_search_hot_key",
                        "study_dialog_search_control",
                        "display_market_status",
                        "header_compare",
                        "edit_buttons_in_legend",
                        "symbol_info",
                        "border_around_the_chart",
                        "main_series_scale_menu",
                        "star_some_intervals_by_default",
                        "datasource_copypaste",
                        "right_bar_stays_on_scroll",
                        "context_menus",
                        "go_to_date",
                        "compare_symbol",
                        "border_around_the_chart",
                        "timezone_menu",
                        //"header_resolutions",//todo: przetestowac
                        //"control_bar",//todo: przetestowac
                        //"edit_buttons_in_legend",//todo: przetestowac
                        "remove_library_container_border","use_localstorage_for_settings"],
      enabled_features: ["study_templates", "dont_show_boolean_study_arguments",
                        "use_localstorage_for_settings",
                        "remove_library_container_border",
                        "save_chart_properties_to_local_storage",
                        "side_toolbar_in_fullscreen_mode",
                        "hide_last_na_study_output",
                        "constraint_dialogs_movement"],
      charts_storage_url: this.chartsStorageUrl,
      charts_storage_api_version: this.chartsStorageApiVersion,
      client_id: this.clientId,
      user_id: this.userId,
      fullscreen: this.fullscreen,
      width:'600',
      height:'400',
      autosize: this.autosize,
      studies_overrides: this.studiesOverrides,
       overrides: {
                        "symbolWatermarkProperties.color": "rgba(0,0,0, 0)",
                        "paneProperties.background": "#20334d",
                        "paneProperties.vertGridProperties.color": "#344568",
                        "paneProperties.horzGridProperties.color": "#344568",
                        "paneProperties.crossHairProperties.color": "#58637a",
                        "paneProperties.crossHairProperties.style": 2,
                        "mainSeriesProperties.style": 9,
                        "mainSeriesProperties.showCountdown": false,
                        "scalesProperties.showSeriesLastValue": true,
                        "mainSeriesProperties.visible": false,
                        "mainSeriesProperties.showPriceLine": false,
                        "mainSeriesProperties.priceLineWidth": 1,
                        "mainSeriesProperties.lockScale": false,
                        "mainSeriesProperties.minTick": "default",
                        "mainSeriesProperties.extendedHours": false,
                        "volumePaneSize": "tiny",
                        editorFontsList: ["Lato", "Arial", "Verdana", "Courier New", "Times New Roman"],
                        "paneProperties.topMargin": 5,
                        "paneProperties.bottomMargin": 5,
                        "paneProperties.leftAxisProperties.autoScale": true,
                        "paneProperties.leftAxisProperties.autoScaleDisabled": false,
                        "paneProperties.leftAxisProperties.percentage": false,
                        "paneProperties.leftAxisProperties.percentageDisabled": false,
                        "paneProperties.leftAxisProperties.log": false,
                        "paneProperties.leftAxisProperties.logDisabled": false,
                        "paneProperties.leftAxisProperties.alignLabels": true,
                        // "paneProperties.legendProperties.showStudyArguments": true,
                        "paneProperties.legendProperties.showStudyTitles": true,
                        "paneProperties.legendProperties.showStudyValues": true,
                        "paneProperties.legendProperties.showSeriesTitle": true,
                        "paneProperties.legendProperties.showSeriesOHLC": true,
                        "scalesProperties.showLeftScale": false,
                        "scalesProperties.showRightScale": true,
                        "scalesProperties.backgroundColor": "#20334d",
                        "scalesProperties.lineColor": "#46587b",
                        "scalesProperties.textColor": "#8f98ad",
                        "scalesProperties.scaleSeriesOnly": false,
                        "mainSeriesProperties.priceAxisProperties.autoScale": true,
                        "mainSeriesProperties.priceAxisProperties.autoScaleDisabled": false,
                        "mainSeriesProperties.priceAxisProperties.percentage": false,
                        "mainSeriesProperties.priceAxisProperties.percentageDisabled": false,
                        "mainSeriesProperties.priceAxisProperties.log": false,
                        "mainSeriesProperties.priceAxisProperties.logDisabled": false,
                        "mainSeriesProperties.candleStyle.upColor": "#3fcfb4",
                        "mainSeriesProperties.candleStyle.downColor": "#fe4761",
                        "mainSeriesProperties.candleStyle.drawWick": true,
                        "mainSeriesProperties.candleStyle.drawBorder": true,
                        "mainSeriesProperties.candleStyle.borderColor": "#3fcfb4",
                        "mainSeriesProperties.candleStyle.borderUpColor": "#3fcfb4",
                        "mainSeriesProperties.candleStyle.borderDownColor": "#fe4761",
                        "mainSeriesProperties.candleStyle.wickColor": "#737375",
                        "mainSeriesProperties.candleStyle.wickUpColor": "#3fcfb4",
                        "mainSeriesProperties.candleStyle.wickDownColor": "#fe4761",
                        "mainSeriesProperties.candleStyle.barColorsOnPrevClose": false,
                        "mainSeriesProperties.hollowCandleStyle.upColor": "#3fcfb4",
                        "mainSeriesProperties.hollowCandleStyle.downColor": "#fe4761",
                        "mainSeriesProperties.hollowCandleStyle.drawWick": true,
                        "mainSeriesProperties.hollowCandleStyle.drawBorder": true,
                        "mainSeriesProperties.hollowCandleStyle.borderColor": "#3fcfb4",
                        "mainSeriesProperties.hollowCandleStyle.borderUpColor": "#3fcfb4",
                        "mainSeriesProperties.hollowCandleStyle.borderDownColor": "#fe4761",
                        "mainSeriesProperties.hollowCandleStyle.wickColor": "#737375",
                        "mainSeriesProperties.hollowCandleStyle.wickUpColor": "#3fcfb4",
                        "mainSeriesProperties.hollowCandleStyle.wickDownColor": "#fe4761",
                        "mainSeriesProperties.haStyle.upColor": "#3fcfb4",
                        "mainSeriesProperties.haStyle.downColor": "#fe4761",
                        "mainSeriesProperties.haStyle.drawWick": true,
                        "mainSeriesProperties.haStyle.drawBorder": true,
                        "mainSeriesProperties.haStyle.borderColor": "#3fcfb4",
                        "mainSeriesProperties.haStyle.borderUpColor": "#3fcfb4",
                        "mainSeriesProperties.haStyle.borderDownColor": "#fe4761",
                        "mainSeriesProperties.haStyle.wickColor": "#737375",
                        "mainSeriesProperties.haStyle.wickUpColor": "#3fcfb4",
                        "mainSeriesProperties.haStyle.wickDownColor": "#fe4761",
                        "mainSeriesProperties.haStyle.barColorsOnPrevClose": false,
                        "mainSeriesProperties.barStyle.upColor": "#3fcfb4",
                        "mainSeriesProperties.barStyle.downColor": "#fe4761",
                        "mainSeriesProperties.barStyle.barColorsOnPrevClose": false,
                        "mainSeriesProperties.barStyle.dontDrawOpen": false,
                        "mainSeriesProperties.lineStyle.color": "#0cbef3",
                        "mainSeriesProperties.lineStyle.linestyle": 0,
                        "mainSeriesProperties.lineStyle.linewidth": 1,
                        "mainSeriesProperties.lineStyle.priceSource": "close",
                        "mainSeriesProperties.areaStyle.color1": "#0cbef3",
                        "mainSeriesProperties.areaStyle.color2": "#0098c4",
                        "mainSeriesProperties.areaStyle.linecolor": "#0cbef3",
                        "mainSeriesProperties.areaStyle.linestyle": 0,
                        "mainSeriesProperties.areaStyle.linewidth": 1,
                        "mainSeriesProperties.areaStyle.priceSource": "close",
                        "mainSeriesProperties.areaStyle.transparency": 80
                    }
    };

    const tvWidget = new widget(widgetOptions);
    this.tvWidget = tvWidget;

    tvWidget.onChartReady(() => {
      const button = tvWidget.createButton()
        .attr('title', 'Click to show a notification popup')
        .addClass('apply-common-tooltip')
        .on('click', () => tvWidget.showNoticeDialog({
          title: 'Notification',
          body: 'TradingView Charting Library API works correctly',
          callback: () => {
            // eslint-disable-next-line no-console
            console.log('Noticed!');
          },
        }));

      button[0].innerHTML = 'Check API';
    });
  },
  destroyed() {
    if (this.tvWidget !== null) {
      this.tvWidget.remove();
      this.tvWidget = null;
    }
  }
}
</script>

<style lang="scss" scoped>
.TVChartContainer {
  height: 500px;
  width:900px;
}
</style>
