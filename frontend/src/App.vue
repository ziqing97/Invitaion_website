<template>
  <router-view></router-view>
</template>

<script>
export default {
name: 'App',
watch: {
    '$route' (to) {
      document.title = to.meta.title || 'Your Website'
      var link = document.querySelector("[rel~='icon']")
      if (!link) {
        link = document.createElement('link');
        link.rel = 'icon';
        document.head.appendChild(link);
      }
      link.setAttribute('href',"http://www.junnuolc.cn/download/logo.jpg")
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
