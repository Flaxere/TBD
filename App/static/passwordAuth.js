function BothFieldsIdenticalCaseSensitive() {
  var one = document.Signup.password1.value;
  var another = document.Signup.password2.value;
  if(one == another) { return true; }
  alert("Oops, both fields must be identical.");
  return false;
  }
  
  function BothFieldsIdenticalCaseInsensitive() {
  var one = document.Signup.password1.value.toLowerCase();
  var another = document.Signup.password2.value.toLowerCase();
  if(one == another) { return true; }
  alert("Oops, both fields must be identical.");
  return false;
  }

  function openForm() {
    document.myForm.style.display = "block";
  }
  
  function closeForm() {
    document.myForm.style.display = "none";
  }