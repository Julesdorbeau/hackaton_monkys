<template>
  <v-card  width="800"
           height="800">
    <v-card-title class="text-h5 grey lighten-2">
    </v-card-title>
    Where can i buy this

    <v-card-text>
      <div class=" mt-12">
        <v-list-item-content>
          <v-list-item-title >vendeur 1</v-list-item-title>

          <v-list-item-subtitle
              class="text--primary"
          >
            vend X
          </v-list-item-subtitle>

          <v-list-item-subtitle > à Y</v-list-item-subtitle>
        </v-list-item-content>

      </div>
      <div class=" mt-12">
        <v-list-item-content>
          <v-list-item-title >vendeur 2</v-list-item-title>

          <v-list-item-subtitle
              class="text--primary"
          >
            vend X
          </v-list-item-subtitle>

          <v-list-item-subtitle > à Y</v-list-item-subtitle>
        </v-list-item-content>

      </div>
      <div class=" mt-12">
        <v-list-item-content>
          <v-list-item-title >vendeur 3</v-list-item-title>

          <v-list-item-subtitle
              class="text--primary"
          >
            vend X
          </v-list-item-subtitle>

          <v-list-item-subtitle > à Y</v-list-item-subtitle>
        </v-list-item-content>

      </div>
      <div >
        <v-list-item-content>
          <v-list-item-title >vendeur 4</v-list-item-title>

          <v-list-item-subtitle
              class="text--primary"
          >
            vend X
          </v-list-item-subtitle>

          <v-list-item-subtitle > à Y</v-list-item-subtitle>
        </v-list-item-content>

      </div>
    </v-card-text>

    <v-divider></v-divider>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
          color="primary"
          text
          @click="dialog3 = false"
      >
        OK
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Vendeur"
}
</script>

<style scoped>

</style>