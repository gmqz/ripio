<template>
    <div id="app">
        <router-view/>
    </div>
</template>

<script>
export default {
    name: 'App',
    data () {
        return {}
    }
}
</script>

<style>
#app {
    width: 100%;
}

/*
 * Base structure
 */

:root {
 --input-padding-x: .75rem;
 --input-padding-y: .75rem;
}

html,
body {
  height: 100%;
}

body {
  display: -ms-flexbox;
  display: flex;
}
</style>
