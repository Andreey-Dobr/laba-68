function makeCloseFunc(alert) {
    return () => alert.remove();
}


function makeAlert(message) {
    let alert = document.createElement('div');
    alert.classList.add('alert');
    alert.innerText = message;

    let closeBtn = document.createElement('button');
    closeBtn.type = 'button';
    closeBtn.innerHTML = '&times;';
    closeBtn.classList.add('close');

    let closeFunc = makeCloseFunc(alert);
    closeBtn.onclick = closeFunc

    alert.appendChild(closeBtn);
    document.body.appendChild(alert);

}


window.addEventListener('load', function() {
    const button = document.getElementById('click_me');
    let lorem = 'Lorem ipsum dolor sit amet consectetur adipisicing, elit. Eius dolor architecto consectetur libero, blanditiis pariatur quas quasi fugit cum repellendus exercitationem tenetur excepturi soluta earum laudantium tempore. Minima, a accusantium voluptatem blanditiis minus recusandae quisquam provident corrupti in ab ea dolorum suscipit eveniet fugit ratione, consequuntur perspiciatis placeat! Earum, tempore.';
    button.onclick = () => makeAlert(lorem);
});

  $.ajax({
    type:"POST",
    url: '/add/',
    data: {
      'username': username
    },
    dataType: 'json',
    success: function (data) {
      if (data.is_taken) {
        alert("A user with this username already exists.");
      }
    }
  });



