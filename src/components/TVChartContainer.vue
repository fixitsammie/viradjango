<template>
  <div>
<div class="TVChartContainer" :id="containerId" />


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
      default: 'USDT-BTC:BITTREX',
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
      default: '/api',
      type: String,
    },
    libraryPath: {
      default: '/static/charting_library/',
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
                        "volume.volume.transparency": 10,
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
      toolbar_bg: '#f4f7f9',
    allow_symbol_change: true,
    theme:"Light",
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
      autosize: this.autosize
      
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
