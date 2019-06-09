<template>
  <div id="app">
      <!-- route outlet -->
      <router-view></router-view>
  </div>
</template>

<script>
import Search from './components/Search.vue'

export default {
  name: 'app',
  components: {
    Search
  }
}
</script>

<style>
.md-content {
  padding: 16px;
}
</style>
