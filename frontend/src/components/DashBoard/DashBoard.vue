<template>
  <v-app id="inspire">

    <v-app-bar class="green lighten-4" app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Amogus</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer
        v-model="drawer"
        fixed
        temporary
    >
      <v-list
          nav
          dense
      >
        <v-list-item-group
            v-model="group"
            active-class="green--text text--accent-4"
        >
          <v-list-item>
            <v-list-item-title>Account</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <Settings/>
          </v-list-item>

          <v-list-item>
            <v-list-item-title href="mailto:jules.dorbeau@epita.fr">Contact us</v-list-item-title>
          </v-list-item>

        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-main class="green lighten-5" >
      <v-container id="main_app">
        <v-row>
          <template v-for="n in 2">
            <v-col
                :key="n"
                class="mt-2"
                cols="12"
            >
              <strong>Category {{ n }}</strong>
            </v-col>

            <v-col
                v-for="j in 6"
                :key="`${n}${j}`"
                cols="6"
                md="2"
            >
                  <v-dialog
                      v-model="dialog"
                      width="500"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-card
                          class="elevation-16 mx-auto"
                          width="300"
                          v-bind="attrs"
                          v-on="on"
                      >
                        <v-card-title class="text-h5">
                         Recipe
                        </v-card-title>
                        <v-card-text>
                          <v-img src="https://picsum.photos/id/11/500/300"></v-img>
                          Lorem ipsum set doloret
                        </v-card-text>

                      </v-card>
                    </template>

                    <v-card>
                      <v-card-title class="text-h5 grey lighten-2">
                      Details
                      </v-card-title>

                      <v-card-text>

                     </v-card-text>

                      <v-divider></v-divider>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                            color="primary"
                            text
                            @click="dialog = false"
                        >
                          I accept
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
            </v-col>
          </template>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Settings from "./Settings";

export default {

  name: 'DashBoard',
data: () => ({ drawer: null }),
components:{
    Settings
}
}
</script>
<style scoped>

</style>