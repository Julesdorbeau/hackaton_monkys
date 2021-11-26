<template>
  <v-row justify="center">
    <v-dialog
        v-model="dialog"
        fullscreen
        hide-overlay
        transition="dialog-bottom-transition"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-list-item-title
            v-bind="attrs"
            v-on="on">Setting</v-list-item-title>
      </template>
      <v-card>
        <v-toolbar
            dark
            color="primary"
        >
          <v-btn
              icon
              dark
              @click="dialog = false"
          >
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>Settings</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn
                dark
                text
                @click="dialog = false"
            >
              Save
            </v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <v-list
            three-line
            subheader
        >
          <v-subheader>User Controls</v-subheader>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>Taste</v-list-item-title>
              <v-list-item-subtitle>tell us more about your taste !</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>Change Password</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-divider></v-divider>
        <v-list
            three-line
            subheader
        >
          <v-subheader>General</v-subheader>
          <v-list-item>

            <v-list-item-content>
              <v-list-item-title>Localisation</v-list-item-title>
              <v-list-item-subtitle>tell us where u at</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>

            <v-list-item-content>
              <v-list-item-title>Budget</v-list-item-title>
              <v-list-item-subtitle>$_$</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

        </v-list>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>


export default {

  name: 'Settings',
  data: () => ({ dialog: false }),

}
</script>

