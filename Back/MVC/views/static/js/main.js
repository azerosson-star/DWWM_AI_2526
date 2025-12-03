window.onload = function () {
  const routerView = document.querySelector('#router-view');

  const btnPicasso = document.querySelector('#btn-picasso');
  const btnCaillebotte = document.querySelector('#btn-caillebotte');
  const btnVermeer = document.querySelector('#btn-vermeer');
  const btnKandinsky = document.querySelector('#btn-kandinsky');
  const btnMonet = document.querySelector('#btn-monet');
  const btnGogh = document.querySelector('#btn-gogh');


  activeMenuItem('btn-picasso');
  const picasso = document.querySelector('#picasso');
  routerView.innerHTML = '';
  routerView.appendChild(picasso.cloneNode(true));

  btnPicasso.addEventListener('click', function () {
    activeMenuItem('btn-picasso');
    const picasso = document.querySelector('#picasso');
    routerView.innerHTML = '';
    routerView.appendChild(picasso.cloneNode(true));
  });

  btnCaillebotte.addEventListener('click', function () {
    activeMenuItem('btn-caillebotte');
    const caillebotte = document.querySelector('#caillebotte');
    routerView.innerHTML = '';
    routerView.appendChild(caillebotte.cloneNode(true));
  });

  btnVermeer.addEventListener('click', function () {
    activeMenuItem('btn-vermeer');
    const vermeer = document.querySelector('#vermeer');
    routerView.innerHTML = '';
    routerView.appendChild(vermeer.cloneNode(true));
  });

  btnKandinsky.addEventListener('click', function () {
    activeMenuItem('btn-kandinsky');
    const kandinsky = document.querySelector('#kandinsky');
    routerView.innerHTML = '';
    routerView.appendChild(kandinsky.cloneNode(true));
  });


  btnMonet.addEventListener('click', function () {
    activeMenuItem('btn-monet');
    const monet = document.querySelector('#monet');
    routerView.innerHTML = '';
    routerView.appendChild(monet.cloneNode(true));
  });

  btnGogh.addEventListener('click', function () {
    activeMenuItem('btn-gogh');
    const gogh = document.querySelector('#gogh');
    routerView.innerHTML = '';
    routerView.appendChild(gogh.cloneNode(true));
  });


  function activeMenuItem(id) {
    const btns = document.querySelectorAll('.nav-menu > a');
    for (const btn of btns) {
      if (btn.id == id) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    }
  }
}