<template>
  <div>
    <md-toolbar className="md-primary">
      <md-field className="md-title">
        <label>Search TV and Movies</label>
        <md-input v-model="searchQuery"></md-input>
        <md-button class="md-icon-button md-dense md-primary">
          <img src="../assets/icon/netflix.png" alt="Netflix">
        </md-button>
        <md-button class="md-icon-button md-dense md-primary">
          <img src="../assets/icon/stan.png" alt="Stan">
        </md-button>
        <md-button class="md-icon-button md-dense md-primary">
          <img src="../assets/icon/prime-video.png" alt="Prime Video">
        </md-button>
        <md-button class="md-icon-button md-dense md-primary">
          <img src="../assets/icon/sbs-on-demand.jpg" alt="SBS On Demand">
        </md-button>
        <md-button class="md-icon-button md-dense md-primary">
          <img src="../assets/icon/abc-iview.png" alt="ABC iView">
        </md-button>
      </md-field>
    </md-toolbar>
    <md-content>
        <div v-for="(item, index) in searchList" :key="index" v-if="item.poster">
          <img :src="'https://images.justwatch.com' + item.poster.replace('{profile}', 's332/' + item.full_path.split('/').pop())"
               :alt="item.title">
        </div>
    </md-content>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    name: 'Search',
    data() {
      return {
        searchQuery: '',
        searchList: [],
        debounce: 0
      };
    },
    watch: {
      searchQuery: {
        handler: function(query) {
          let self = this;
          self.searchList = [];
          if (self.debounce > 0) clearTimeout(this.debounce);
          if (query === "") return;
          this.debounce = setTimeout(function () {
            axios.get("search/tv/" + query)
                 .then(response => self.searchList = response.data.items);
            }, 800);
        }
      }
    }
  };
</script>

<style>
  .md-content div {
    width: 296px;
    margin: 8px;
    display: inline-block;
    vertical-align: top;
  }
</style>