<template>
  <section class="container">
  <h2 id="title">Publishers</h2>
<ul>
     <li v-for="item in persons">
    {{ item.first_name }}
    </li>
</ul>
<!--
    <div>
      <logo/>
      <h1 class="title">
        sitedjangofrontend
      </h1>
      <h2 class="subtitle">
        siteDjango
      </h2>

      <div class="links">
        <a href="https://nuxtjs.org/" target="_blank" class="button--green">Documentation</a>
        <a href="https://github.com/nuxt/nuxt.js" target="_blank" class="button--grey">GitHub</a>
      </div>
    </div> -->
  </section>
</template>

<script>
import Logo from '~/components/Logo.vue'
import axios from 'axios'

export default {
  computed: {
    persons () { return this.$store.state.persons }
  },
  components: {
    Logo
  },
  async fetch ({ store, params }) {
    let { data } = await axios.get('http://127.0.0.1:8000/api/persons/?format=json&pk=' + params.id)
    console.log('http://127.0.0.1:8000/api/persons/?format=json&pk=' + params.id)
    store.commit('set', data)
  }
}
</script>

<style>
.container
{
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.title
{
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; /* 1 */
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}
.subtitle
{
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}
.links
{
  padding-top: 15px;
}
</style>
