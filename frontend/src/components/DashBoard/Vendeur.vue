<template>
  <v-card  width="800"
           height="800">
    <v-card-title class="text-h5 grey lighten-2">
    </v-card-title>
    Where can i buy this

    <v-card-text>
        <v-simple-table>
          <template v-slot:default>
            <thead>
            <tr>
              <th class="text-left">
                Name
              </th>
              <th class="text-left">
                product
              </th>
            </tr>
            </thead>
            <tbody>
            <tr
                v-for="item in desserts"
                :key="item.name"
            >
              <td>{{ item.name }}</td>
              <td>{{ item.calories }}</td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>

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
  name: "Vendeur",
  data(){ return {
    desserts: [
      {
        name: 'la maman de jules',
        calories: 'des calins',
      },
      {
        name: 'Ferme de X',
        calories: 'poulet',
      },
      {
        name: 'Ferme de Y',
        calories: 'legume',
      },
      {
        name: 'Verger du Y',
        calories: 'fruit',
      },
      {
        name: 'Coteau de machin',
        calories: 'vin',
      }
    ],}
}}
</script>

<style scoped>

</style>