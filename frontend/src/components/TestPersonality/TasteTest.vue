<template>
  <v-app>
    <v-main class="green lighten-5" id="main_app">
      <v-container >
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12 green lighten-5" v-if="!this.localisation_done">
              <v-toolbar dark color="green lighten-4">
                <v-toolbar-title>Where u at bitch ?</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                  <template>

                      <v-btn
                          class="mx-2"
                          fab
                          large
                          color="green lighten-4"
                          @click="get_localisation();"
                      >
                        <v-icon dark>
                          mdi-map
                        </v-icon>
                      </v-btn>
                  </template>
                </v-card-text>
            </v-card>
            <v-card class="elevation-12 green lighten-5" v-if="this.localisation_done">
              <v-toolbar dark color="green lighten-4">
                <v-toolbar-title>Tell us more about U</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <template>
                  <v-card
                      class="mx-auto  "
                      max-width="400"
                  >
                    <v-img
                        class="white--text align-end"
                        height="200px"
                        :src="this.dish"
                    >
                      <v-card-title>Consider the Following</v-card-title>
                    </v-img>
                    <div >
                    <v-card-subtitle id="titre_plat" class="pb-0">
                      Soupe de Potiron
                    </v-card-subtitle>

                    <v-card-text  class="text--primary">
                      <div id="prix_portion">3e par portion</div>

                      <div id="kcal">140kcal</div>
                    </v-card-text>

                    <v-card-actions>
                      <v-btn
                          color="orange"
                          text
                          @click="Change_dish()"
                      >
                        🤮
                      </v-btn>
                      <v-spacer></v-spacer>
                      <v-btn
                          color="orange"
                          text
                          @click="Change_dish()"
                      >
                        😬
                      </v-btn>
                      <v-spacer></v-spacer>
                      <v-btn
                          color="orange"
                          text
                          @click="Change_dish()"
                      >
                        😊
                      </v-btn>
                      <v-spacer></v-spacer>
                      <v-btn
                          color="orange"
                          text
                          @click="Change_dish();"
                      >
                        😋
                      </v-btn>
                    </v-card-actions>
                    </div>
                  </v-card>
                </template>
              </v-card-text>
            </v-card>

          </v-flex>
        </v-layout>
      </v-container>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {

  name: "TasteTest",
  components:{

},

  data() {
    return {
      position :false,
      myPosition: null,
      display_loc: false,
      localisation_done:false,
       drawer: null ,
      compteur:0,
      dish:"https://www.papillesetpupilles.fr/wp-content/uploads/2013/11/Soupe-au-potiron-%C2%A9Ekaterina-Kondratova-shutterstock.jpg",
      potiron: "https://www.papillesetpupilles.fr/wp-content/uploads/2013/11/Soupe-au-potiron-%C2%A9Ekaterina-Kondratova-shutterstock.jpg",
      pizza: "https://www.letribunaldunet.fr/wp-content/uploads/2020/05/pizza.jpg",
      pates:"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.LqBChOM13IQnTQEhsm6hCAHaFt%26pid%3DApi&f=1",
      boeufB: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.5puvpRB52zk5SNBeUEe1HAHaE6%26pid%3DApi&f=1",
      ratatouille:"https://www.marmitedumonde.com/wp-content/uploads/2016/09/ratatouille-provencale-vraie-recette.jpg",

      coutpotiron:"3$",
      coutpizza:"5$",
      coutpates:"4$",
      coutboeufB:"6$",
      coutratatouille:"3",
      kcalpotiron:"134kcal",
      kcalpizza:"400kcal",
      kcalpates:"300kcal",
      kcalboeuf:"300kcal",
      kcalratatouille:"400kcal"
    }},
methods: {
  display_loc_please(){
    this.display_loc=!this.display_loc
  },
  get_localisation(){
    var error=false
    navigator.geolocation.getCurrentPosition((position) => {
      // return the coordinates
      this.myPosition = position.coords;
      console.log(this.myPosition)
      this.position=true


    }, (error) => {
      // check if the user denied geolocation, or if there was any other problem
      if (error.code == error.PERMISSION_DENIED) {
        error=true
        alert('Geolocation has been disabled on this page, please review your browser\'s parameters');
      } else {
        error=true
        alert('Unable to find your position, try again later.');
      }
    }, {
      timeout: 10000
    });
    this.localisation_done=!error
  },
  Change_dish(){
    if(this.compteur==4){
      this.$router.replace({ name: "dashboard", params: { username: this.coutratatouille } });
    }
    var title = document.getElementById("titre_plat")
    var prix= document.getElementById("prix_portion")
    var kcal= document.getElementById("kcal")
    this.compteur++

    switch (this.compteur){
      case 0:
          title.innerText="Soupe de potirons"
          prix.innerText=this.coutpotiron
          kcal.innerText=this.kcalpotiron
          break
      case 1:
        this.dish=this.pizza
        title.innerText="pizza vegan"
        prix.innerText=this.coutpizza
        kcal.innerText=this.kcalpizza
        break
      case 2:
        this.dish=this.pates
            title.innerText="pates au légumes frait"
            prix.innerText=this.coutpates
            kcal.innerText=this.kcalpotiron
            break
      case 3:
           this.dish= this.boeufB
            title.innerText="boeuf bourguignon"
            prix.innerText=this.coutboeufB
            kcal.innerText=this.kcalboeuf
            break
      case 4:
       this.dish= this.ratatouille
        title.innerText="ratatouille"
            prix.innerText=this.coutratatouille
            kcal.innerText=this.kcalratatouille
            break
    }

  }
  }}
</script>
<style scoped>
#main_app {
background: url('https://c.pxhere.com/photos/1e/84/corn_crops_farm_field_food-979172.jpg!d');
background-size: cover;
width: 100%;
height: 100%;
}</style>