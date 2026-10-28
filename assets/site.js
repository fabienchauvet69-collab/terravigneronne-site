(function(){
  var t=document.querySelector('.nav-toggle'),m=document.getElementById('menu');
  if(t&&m){t.addEventListener('click',function(){var o=m.classList.toggle('open');t.setAttribute('aria-expanded',o?'true':'false');});}
  var p=new URLSearchParams(location.search),s=p.get('envoi'),box=document.getElementById('form-status');
  if(box&&s){box.hidden=false;box.className='alert '+(s==='ok'?'alert-ok':'alert-err');
    box.textContent=s==='ok'?'Merci, votre message est bien parti. Nous revenons vers vous très vite.':'Le message n’a pas pu être envoyé. Écrivez-nous directement à contact@terravigneronne.com ou appelez le 07 49 10 83 09.';}
})();
