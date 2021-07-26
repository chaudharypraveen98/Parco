//auto increment
var firebaseConfig = {
  apiKey: "",
  authDomain: "",
  databaseURL: "",
  projectId: "",
  storageBucket: "",
  messagingSenderId: "",
  appId: "",
  measurementId: ""
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

$(document).ready(function(){
  let database = firebase.database();
  let slot1;
  let slot2;
  let slot3;
  let slot4;
  let len1,len2,len3,len4;

  database.ref().on("value", function(snap){
    slot1 = snap.val().slot1;
    slot2 = snap.val().slot2;
    slot3 = snap.val().slot3;
    slot4 = snap.val().slot4;
    len1 = document.getElementsByClassName("slot1").length;
    len2 = document.getElementsByClassName("slot2").length;
    len3 = document.getElementsByClassName("slot3").length;
    len4 = document.getElementsByClassName("slot4").length;
    insertOption(len1, slot1, "slot1");
    insertOption(len2, slot2, "slot2");
    insertOption(len3, slot3, "slot3");
    insertOption(len4, slot4, "slot4");
    console.log("-----------");
  });
  let insertOption=function (length,slotValue,slotTitle) {
    console.log("value",length,slotTitle,slotValue);
    if (length!=0){
        if(slotValue !="free"){
          console.log("removing free");
          removeSlot(slotTitle);
      } else {
          console.log("already free")
        }
    } else{
        if(slotValue ==="free"){
          console.log("inserting new")
          insertSlot(slotTitle);
      } else {
        console.log("already occupied")
      }
    }
  }
  let insertSlot=function (param){
    $('#id_slot_no').append(
      $('<option>').prop({
        value : param,
        innerHTML: `${param}`,
        className: param,
      })
    );
  };
  let removeSlot=function (param){
    $(`.${param}`).remove()
  };
});