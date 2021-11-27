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
                    </v-img>
                    <div >
                    <v-card-subtitle id="titre_plat" class="pb-0">
                      Fettuccine with Lamb and Mint
                    </v-card-subtitle>

                    <v-card-text  class="text--primary">
                      <div id="prix_portion">3e par portion</div>

                      <div id="kcal">140kcal</div>
                    </v-card-text>

                    <v-card-actions>
                      <v-btn
                          color="orange"
                          text
                          @click="Push_Note(0);Change_dish()"
                      >
                        🤮
                      </v-btn>
                      <v-spacer></v-spacer>
                      <v-btn
                          color="orange"
                          text
                          @click="Push_Note(1);Change_dish()"
                      >
                        😬
                      </v-btn>
                      <v-spacer></v-spacer>
                      <v-btn
                          color="orange"
                          text
                          @click="Push_Note(2);Change_dish()"
                      >
                        😊
                      </v-btn>
                      <v-spacer></v-spacer>
                      <v-btn
                          color="orange"
                          text
                          @click="Push_Note(3);Change_dish();"
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
      notes:[],
      position :false,
      myPosition: null,
      display_loc: false,
      localisation_done:false,
       drawer: null ,
      compteur:0,
      dish:"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.platingsandpairings.com%2Fwp-content%2Fuploads%2F2018%2F10%2Finstant-pot-pasta-lamb-mint-7.jpg&f=1&nofb=1",
      fettucine_lamb: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.platingsandpairings.com%2Fwp-content%2Fuploads%2F2018%2F10%2Finstant-pot-pasta-lamb-mint-7.jpg&f=1&nofb=1",
      risotto: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.a9H4QiGh27nJUhHt1fV6ggHaE8%26pid%3DApi&f=1",
      californian_burger:"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.hellofresh.com%2Ff_auto%2Cfl_lossy%2Ch_640%2Cq_auto%2Cw_1200%2Fhellofresh_s3%2Fimage%2Fburgers-de-dinde-a-la-californienne-a883ed14.jpg&f=1&nofb=1",
      California_Quesadilla: "https://i.pinimg.com/originals/2e/d7/cd/2ed7cda58c8d6db2b41bf01bfd3019cc.jpg",
      Crab_Linguine  :"http://cdn.sheknows.com/articles/2015/08/Rebekah/Experts/pasta-1.jpg",
      Fudge_Brownie_Pie:"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi1.wp.com%2Fthebestblogrecipes.com%2Fwp-content%2Fuploads%2F2016%2F12%2FFudge-Brownie-Pie-Recipe.jpg%3Fresize%3D600%252C900&f=1&nofb=1",
      coutfettucine_lamb:"3$",
      coutrisoto:"5$",
      coutcalifornian_burger:"4$",
      coutCalifornia_Quesadilla:"6$",
      coutCrab_Linguine:"3",
      cout_Fudge_Brownie_Pie:"5",
      kcalfettucine_lamb:"134kcal",
      kcalrisoto:"400kcal",
      kcalcalifornian_burger:"300kcal",
      kcalCalifornia_Quesadilla:"300kcal",
      kcalCrab_Linguine:"400kcal",
      kcalFudge_Brownie_Pie:"5",
    }},
methods: {
  display_loc_please(){
    this.display_loc=!this.display_loc
  },
  get_localisation(){
    this.localisation_done=true
    navigator.geolocation.getCurrentPosition((position) => {
      // return the coordinates
      this.myPosition = position.coords;
      console.log(this.myPosition)
      var array=[]
      array.push(this.myPosition.latitude,this.myPosition.longitude)
      var stringbody ="{ latitude: 49.0925712, longitude: 1.4816335 }"
      console.log(stringbody)
      this.position=true
      fetch('http://127.0.0.1:5000/localisation', {
        method: 'POST', // or 'PUT'
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(array),
      })
          .then(response => response.json())
          .then(data => {
            console.log('Success:', data);
          })
          .catch((error) => {
            console.error('Error:', error);
          });

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

  },
  Push_Note(note){
    this.notes.push(note)
  },
  Change_dish(){
    if(this.compteur==5){
      fetch('http://127.0.0.1:5000/taste', {
        method: 'POST', // or 'PUT'
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.notes),
      })
          .then(response => response.json())
          .then(data => {
            console.log('Success:', data);
          })
          .catch((error) => {
            console.error('Error:', error);
          });

      this.$router.replace({ name: "dashboard", params: { username: this.coutratatouille } });
    }
    const title = document.getElementById("titre_plat");
    const prix= document.getElementById("prix_portion")
    const kcal= document.getElementById("kcal")
    this.compteur++

    switch (this.compteur){
      case 0:
          title.innerText="Fettuccine with Lamb and Mint"
          prix.innerText=this.coutfettucine_lamb
          kcal.innerText=this.kcalfettucine_lamb
          break
      case 1:
        this.dish=this.risotto
        title.innerText="Risotto Con Frutti Di Mare\n"
        prix.innerText=this.coutrisoto
        kcal.innerText=this.kcalrisoto
        break
      case 2:
        this.dish=this.californian_burger
            title.innerText="California-Style Turkey Burger\n"
            prix.innerText=this.coutcalifornian_burger
            kcal.innerText=this.kcalcalifornian_burger
            break
      case 3:
           this.dish= this.California_Quesadilla
            title.innerText="California Quesadilla\n"
            prix.innerText=this.coutCalifornia_Quesadilla
            kcal.innerText=this.kcalCalifornia_Quesadilla
            break
      case 4:
       this.dish= this.Crab_Linguine

            title.innerText="Crab Linguine\n"
            prix.innerText=this.coutCrab_Linguine
            kcal.innerText=this.kcalCrab_Linguine
            break
      case 5:
        this.dish= this.Fudge_Brownie_Pie
            title.innerText="Fudge Brownie Pie"
            kcal.innerText=this.kcalFudge_Brownie_Pie
            break;
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