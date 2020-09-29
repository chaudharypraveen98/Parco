//auto increment
var firebaseConfig = {
  apiKey: "AIzaSyD9v4wGnOfvPj5hFvT9RFHr51RHh3VhzxE",
  authDomain: "smart-parking-51b36.firebaseapp.com",
  databaseURL: "https://smart-parking-51b36.firebaseio.com",
  projectId: "smart-parking-51b36",
  storageBucket: "smart-parking-51b36.appspot.com",
  messagingSenderId: "896172750089",
  appId: "1:896172750089:web:107f3613b8b66ac74c0fd8",
  measurementId: "G-ZCV4DBC045"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

$(document).ready(function(){
  let database = firebase.database();
  let slot1;
  let slot2;
  let slot3;
  let slot4;

  database.ref().on("value", function(snap){
    slot1 = snap.val().slot1;
    slot2 = snap.val().slot2;
    slot3 = snap.val().slot3;
    slot4 = snap.val().slot4;
    console.log(slot1);

    {if(slot1 ==="free"){
      console.log("free");
      insertSlot("slot1");
    } else {
      console.log("occupied");
      removeSlot("slot1");
    }}
    {if(slot2 ==="free"){
      console.log("free");
      insertSlot("slot2");
    } else {
      console.log("occupied");
      removeSlot("slot2");
    }}
    {if(slot3 ==="free"){
      console.log("free");
      insertSlot("slot3");
    } else {
      console.log("occupied");
      removeSlot("slot3");
    }}
    {if(slot4 ==="free"){
      console.log("free");
      insertSlot("slot4");
    } else {
      console.log("occupied");
      removeSlot("slot4");
    }}
  });
  let insertSlot=function (param){
    console.log(param)
    $('#id-slot').append(
      $('<option>').prop({
        id: param,
        innerHTML: "slot1 activated",
        name: param,
      })
    );
  };
  let removeSlot=function (param){
    $(`#${param}`).remove()
  };
});