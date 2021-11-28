<template>
  <v-app id="inspire" class="">
    <div v-if="!this.recipes_arrived">
      <TasteTest @on-recipes-change="this.recipes_changed"></TasteTest>
    </div>
<div v-if="this.recipes_arrived"   class="amogus" >
    <v-app-bar class="green lighten-4" app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Miam</v-toolbar-title>
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

    <v-main class="" >
      <v-container id="main_app">
        <v-row>
          <template >
            <v-col

                class="mt-2"
                cols="12"
            >
              <strong>Recipe</strong>
            </v-col>

            <v-col

                cols="6"
                md="2"
            >
                  <v-dialog
                      v-model="dialog1"
                      width="500"
                  >

                    <template v-slot:activator="{ on, attrs }">
                      <v-card
                          class="elevation-16 mx-auto"
                          width="300"
                          v-bind="attrs"
                          v-on="on"
                      >
                        <v-card-title id="r1_title" class="text-h6" >
                          {{ recipes[0] }}
                        </v-card-title>
                        <v-card-text>
                          <v-img src="https://picsum.photos/id/11/500/300"></v-img>

                        </v-card-text>

                      </v-card>
                    </template>

                    <Vendeur></Vendeur>
                  </v-dialog>
              <v-rating
                  @input="this.NewGrade"
                  v-model="rating1"
                  color="yellow darken-3"
                  background-color="grey darken-1"
                  empty-icon="$ratingFull"

                  hover
                  small
              ></v-rating>
            </v-col>

            <v-col

                cols="6"
                md="2"
            >
              <v-dialog
                  v-model="dialog2"
                  width="500"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-card
                      class="elevation-16 mx-auto"
                      width="300"

                      v-bind="attrs"
                      v-on="on"
                  >
                    <v-card-title id="r2_title" class="text-h6">
                      {{ recipes[1] }}
                    </v-card-title>
                    <v-card-text>
                      <v-img src="https://picsum.photos/id/11/500/300"></v-img>

                    </v-card-text>

                  </v-card>
                </template>
                <Vendeur></Vendeur>
              </v-dialog>
              <v-rating
                  @input=" this.NewGrade"
                  v-model="rating2"
                  color="yellow darken-3"
                  background-color="grey darken-1"
                  empty-icon="$ratingFull"
                  hover
                  small
              ></v-rating>
            </v-col>

            <v-col

                cols="6"
                md="2"
            >
              <v-dialog
                  v-model="dialog3"
                  width="800"
                  height="800"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-card
                      class="elevation-16 mx-auto"
                      width="300"
                      v-bind="attrs"
                      v-on="on"
                  >
                    <v-card-title id="r3_title" class="text-h6">
                      {{ recipes[2] }}
                    </v-card-title>
                    <v-card-text>
                      <v-img src="https://picsum.photos/id/11/500/300"></v-img>

                    </v-card-text>

                  </v-card>
                </template>

                <Vendeur></Vendeur>
              </v-dialog>
              <v-rating
                  @input="this.NewGrade"
                  v-model="rating3"
                  color="yellow darken-3"
                  background-color="grey darken-1"
                  empty-icon="$ratingFull"
                  hover
                  small
              ></v-rating>
            </v-col>

            <v-col

                cols="6"
                md="2"
            >
              <v-dialog
                  v-model="dialog4"
                  width="500"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-card
                      class="elevation-16 mx-auto"
                      width="300"
                      v-bind="attrs"
                      v-on="on"
                  >
                    <v-card-title id="r4_title" class="text-h6">
                      {{ recipes[3] }}
                    </v-card-title>
                    <v-card-text>
                      <v-img src="https://picsum.photos/id/11/500/300"></v-img>

                    </v-card-text>

                  </v-card>
                </template>

               <Vendeur/>
              </v-dialog>
              <v-rating
                  @input="this.NewGrade"
                  v-model="rating4"
                  color="yellow darken-3"
                  background-color="grey darken-1"
                  empty-icon="$ratingFull"
                  hover
                  small
              ></v-rating>
            </v-col>

            <v-col

                cols="6"
                md="2"
            >
              <v-dialog
                  v-model="dialog5"
                  width="500"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-card
                      class="elevation-16 mx-auto"
                      width="300"
                      v-bind="attrs"
                      v-on="on"
                  >
                    <v-card-title id="r5_title" class="text-h6">
                      {{ recipes[4] }}
                    </v-card-title>
                    <v-card-text>
                      <v-img src="https://picsum.photos/id/11/500/300"></v-img>

                    </v-card-text>

                  </v-card>
                </template>
                <Vendeur></Vendeur>
              </v-dialog>
              <v-rating
                  @input="this.NewGrade"
                  v-model="rating5"
                  color="yellow darken-3"
                  background-color="grey darken-1"
                  empty-icon="$ratingFull"
                  hover
                  small
              ></v-rating>
            </v-col>

            <v-col

                cols="6"
                md="2"
            >
              <v-dialog
                  v-model="dialog6"
                  width="500"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-card
                      class="elevation-16 mx-auto"
                      width="300"
                      v-bind="attrs"
                      v-on="on"
                  >
                    <v-card-title id="r6_title" class="text-h6">
                      {{ recipes[5] }}
                    </v-card-title>
                    <v-card-text>
                      <v-img src="https://picsum.photos/id/11/500/300"></v-img>

                    </v-card-text>

                  </v-card>
                </template>
                <Vendeur></Vendeur>
              </v-dialog>
              <v-rating
                  @input="this.NewGrade"
                  v-model="rating6"
                  color="yellow darken-3"
                  background-color="grey darken-1"
                  empty-icon="$ratingFull"
                  hover
                  small
              ></v-rating>
            </v-col>

            <v-col

                cols="6"
                md="2"
            >
              <v-dialog
                  v-model="dialog7"
                  width="500"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-card
                      class="elevation-16 mx-auto"
                      width="300"
                      v-bind="attrs"
                      v-on="on"
                  >
                    <v-card-title id="r7_title" class="text-h6">
                      {{ recipes[6] }}
                    </v-card-title>
                    <v-card-text>
                      <v-img src="https://picsum.photos/id/11/500/300"></v-img>

                    </v-card-text>

                  </v-card>
                </template>

                <Vendeur></Vendeur>
              </v-dialog>
              <v-rating
                  @input="this.NewGrade "
                  v-model="rating7"
                  color="yellow darken-3"
                  background-color="grey darken-1"
                  empty-icon="$ratingFull"
                  hover
                  small
              ></v-rating>
            </v-col>
          </template>
        </v-row>
      </v-container>
    </v-main>
</div>
  </v-app>
</template>

<script>
import Settings from "./Settings";
import TasteTest from "../TestPersonality/TasteTest";
import Vendeur from "./Vendeur";
export default {

  name: 'DashBoard',
data: () => ({
  dialog1:null,
  attrs1:null,
  on1 :null,
  dialog2:null,
  attrs2:null,
  on2 :null,
  dialog3:null,
  attrs3:null,
  on3 :null,
  dialog4:null,
  attrs4:null,
  on4 :null,
  dialog5:null,
  attrs5:null,
  on5 :null,
  dialog6:null,
  attrs6:null,
  on6 :null,
  dialog7:null,
  attrs7:null,
  on7 :null,
  drawer: null,
  recipes_arrived:false,
  recipes:[],
  rating1:0,
  rating2:0,
  rating3:0,
  rating4:0,
  rating5:0,
  rating6:0,
  rating7:0,
}),

  components:{
    TasteTest,
    Settings,
    Vendeur
},created() {
    console.log("this is my recipes :"+ this.recipes)
  },
  mounted() {
    var r1= document.getElementById("r1_title")
    var r2= document.getElementById("r2_title")
    var r3= document.getElementById("r3_title")
    var r4= document.getElementById("r4_title")
    var r5= document.getElementById("r5_title")
    var r6= document.getElementById("r6_title")
    var r7= document.getElementById("r7_title")
    r1.innerText=this.recipes[0]
    r2.innerText=this.recipes[1]
    r3.innerText=this.recipes[2]
    r4.innerText=this.recipes[3]
    r5.innerText=this.recipes[4]
    r5.innerText=this.recipes[5]
    r6.innerText=this.recipes[6]
    r7.innerText=this.recipes[7]

  },
  props:{
  a: Array
},
  methods: {
    recipes_changed(e){
      this.recipes_arrived=true
      console.log("this is what i've received witht the event " + e)
      var bascule=true
      var array=String(e).split(',')
      console.log("new array")
      console.log(array)
      for (var  index = 0; index < array.length; index++) {
        console.log(array[index]);
        if(bascule){
          this.recipes.push(array[index])
          console.log("j'add ça :"+array[index])
          bascule=false
        }else{
          bascule=true
        }
      }
      this.recipes_arrived=true
      var r1= document.getElementById("r1_title")
      var r2= document.getElementById("r2_title")
      var r3= document.getElementById("r3_title")
      var r4= document.getElementById("r4_title")
      var r5= document.getElementById("r5_title")
      var r6= document.getElementById("r6_title")
      var r7= document.getElementById("r7_title")
      r1.innerText=this.recipes[0]
      r2.innerText=this.recipes[1]
      r3.innerText=this.recipes[2]
      r4.innerText=this.recipes[3]
      r5.innerText=this.recipes[4]
      r5.innerText=this.recipes[5]
      r6.innerText=this.recipes[6]
      r7.innerText=this.recipes[7]
    },

  NewGrade(){
    console.log("somebody grade something")
    if(this.rating1&&this.rating2&&this.rating3&&this.rating4&&this.rating5&&this.rating6&&this.rating7){
      console.log("OWO now we serious")
      var sendme=[]
      sendme.push(this.recipes[0]+":"+this.rating1)
      sendme.push(this.recipes[1]+":"+this.rating2)
      sendme.push(this.recipes[2]+":"+this.rating3)
      sendme.push(this.recipes[3]+":"+this.rating4)
      sendme.push(this.recipes[4]+":"+this.rating5)
      sendme.push(this.recipes[5]+":"+this.rating6)
      sendme.push(this.recipes[6]+":"+this.rating7)
      console.log("sending this :"+sendme)
      fetch('http://127.0.0.1:5000/taste', {
        method: 'POST', // or 'PUT'
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(sendme),
      })
          .then(response => response.json())
          .then(data => {
            console.log('Success oui oui :', data);
            console.log("emeting")
            this.recipes_changed(data)
            this.rating1=0
            this.rating2=0
            this.rating3=0
            this.rating4=0
            this.rating5=0
            this.rating6=0
            this.rating7=0
          })
          .catch((error) => {
            console.error('Error:', error);
          });
    }
    }
  }
}
</script>
<style scoped>
.amogus {
  background: url('https://c.pxhere.com/photos/1e/84/corn_crops_farm_field_food-979172.jpg!d');
  background-size: cover;
  width: 100%;
  height: 100%;
}</style>