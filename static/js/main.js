document.addEventListener('DOMContentLoaded',()=>{
  const smoothLinks=document.querySelectorAll('a[href^="#"]');
  smoothLinks.forEach(link=>{
     link.addEventListener('click',(e)=>{
        const target=document.querySelector(link.getAttribute('href'));
        if(target){e.preventDefault();target.scrollIntoView({behavior:'smooth'});}
     });
  });
});