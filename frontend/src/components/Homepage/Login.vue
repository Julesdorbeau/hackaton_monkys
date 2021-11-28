<template>
   <v-app >
      <v-main>
         <v-container fluid fill-height class ="main_app">
            <v-layout align-center justify-center>
               <v-flex xs12 sm8 md4>
                  <v-card class="elevation-12">
                     <v-toolbar dark color="green">
                        <v-toolbar-title>Login</v-toolbar-title>
                     </v-toolbar>
                     <v-card-text>
                     <form ref="form" @submit.prevent="isRegister ? register() : login()">
                            <v-text-field
                              v-model="username"
                              name="username"
                              label="Username"
                              type="text"
                              placeholder="username"
                              required
                           ></v-text-field>
                           
                            <v-text-field
                              v-model="password"
                              name="password"
                              label="Password"
                              type="password"
                              placeholder="password"
                              required
                           ></v-text-field>

                           <v-text-field v-if="isRegister"
                              v-model="confirmPassword"
                              name="confirmPassword"
                              label="Confirm Password"
                              type="password"
                              placeholder="cocnfirm password"
                              required
                           ></v-text-field>
                           <div class="red--text"> {{errorMessage}}</div>
                           <v-btn type="submit" class="mt-4" dark color="green" value="log in">{{isRegister ? stateObj.register.name : stateObj.login.name}}</v-btn>
                           <div class="grey--text mt-4" v-on:click="isRegister = !isRegister;">
                              {{toggleMessage}}  
                           </div>
                      </form>
                     </v-card-text>
                  </v-card>
                
               </v-flex>
            </v-layout>
         </v-container>
      </v-main>
   </v-app>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      username: "",
      password: "",
      confirmPassword: "",
      isRegister : false,
      errorMessage: "",
      stateObj: {
         register :{
            name: 'Register',
            message: 'Aleady have an Acoount? login.'
         },
         login : {
            name: 'Login',
            message: 'Register'
         }
      }
    };
  },
  methods: {
    login() {
      this.$router.replace({ name: "dashboard", params: { } });
    },
    register() {
       if(this.password == this.confirmPassword){
          this.isRegister = false;
          this.errorMessage = "";
          this.$refs.form.reset();
         this.$router.replace({ name: "dashboard", params: { } });
       }
       else {
         this.errorMessage = "password did not match"
       }
    }
  },
      computed: {
       toggleMessage : function() { 
          return this.isRegister ? this.stateObj.register.message : this.stateObj.login.message }
    }
};
</script>
<style scoped>
.main_app {
  background: url('https://c.pxhere.com/photos/1e/84/corn_crops_farm_field_food-979172.jpg!d');
  background-size: cover;
  width: 100%;
  height: 100%;
}
</style>