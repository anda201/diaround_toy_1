const drop_icon = document.querySelector('.drop-icon')
const drop_menu = document.querySelector('.dropdown-menu')

drop_icon.addEventListener('click', (event) =>{
  drop_menu.style.display = 'block';
  event.stopPropagation();
});

document.addEventListener('click', (event) =>{
  if (!drop_menu.contains(event.target)) {
    drop_menu.style.display = 'none';
  }
});

drop_menu.addEventListener('click', (event) =>{
  event.stopPropagation();
});