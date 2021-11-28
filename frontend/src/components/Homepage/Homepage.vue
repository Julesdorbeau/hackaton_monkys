<template>
  <v-app id="app">

    <v-container fluid fill-height class="homepage" style="height: 100%;">
      <v-layout justify-center align-center column pa-5>
        <div class="display-4 font-weight-black white--text text-xs-center">
          HEALTHY AND LOCALS MEALS
        </div>
        <div
            class="display-4 font-weight-black white--text text-xs-center mb-3"
        >
          FOR YOUR TABLE
        </div>
        <div class="display-1 font-weight-bold white--text text-xs-center">
          With Hanuman, re-etasblish a link with local productor and discover a new world of flavours
        </div>
        <v-btn  class="mt-5 " color="green lighten-2"  to="/Login">
          <v-icon large color="white">Let's go </v-icon>
        </v-btn>
      </v-layout>
    </v-container>
  </v-app>
</template>
<script>
export default {
}
</script>
<style scoped>
.homepage {
  background: url('https://c.pxhere.com/photos/1e/84/corn_crops_farm_field_food-979172.jpg!d');
  background-size: cover;
  width: 100%;
  height: 100%;
}
</style>