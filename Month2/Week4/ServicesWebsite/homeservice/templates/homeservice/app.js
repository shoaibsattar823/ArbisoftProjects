<script>
$('#btn').on('click', function(){
  $.ajax({
    url: '/example/data/',
    // data: 'data.txt',
    success: function(data){
      console.log(data.data);
      document.getElementById('more').innerHTML = data.data;
    }
  });
});

$(document).ready(function(){

  $('img').hover(function(){
    console.log("inside the image");
  }, function(){
    console.log("outside the image");
  });

  $('#id_register').on('click', function(evt){
    var uname, email, pass, pass2, text;
    uname = $('#uname').val();
    email = $('#uemail').val();
    pass = $('#upassword').val();
    pass2 = $('#upassword2').val();
    console.log('here'+uname);
    if (uname === ''){
      $('#uname').css('border-color', 'red');
      evt.preventDefault(evt);
      document.getElementById("testuser").innerHTML = 'Invalid Username';
    }
    if (email === ''){
      $('#uemail').css('border-color', 'red');
      evt.preventDefault(evt);
      document.getElementById("testemail").innerHTML = 'Invalid email';
    }
    if (pass === ''){
      $('#upassword').css('border-color', 'red');
      evt.preventDefault(evt);
      document.getElementById("testpass").innerHTML = 'Invalid password';
    }
    if (pass2 === ''){
      $('#upassword2').css('border-color', 'red');
      evt.preventDefault(evt);
      document.getElementById("testpass2").innerHTML = 'Invalid password';
    }

  })
});


</script>
