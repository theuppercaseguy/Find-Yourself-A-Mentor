function clear_admin_tables(){
   var butts = document.querySelectorAll('.tables-buttons .tables-section .tables');
      
   [].forEach.call(butts, function(butts){
   
       butts.style.display='none';
   
   })
}



clear_admin_tables();
      
document.getElementById('table1').style.display='block';



document.getElementById('button-1').onclick= () =>{
   clear_admin_tables();
   console.log('asdf0');
   document.getElementById('table1').style.display='block';
}

document.getElementById('button-2').onclick= () =>{
   clear_admin_tables();
   document.getElementById('table2').style.display='block';
}

document.getElementById('button-3').onclick= () =>{
   clear_admin_tables();
   document.getElementById('table3').style.display='block';
}
document.getElementById('button-4').onclick= () =>{
   clear_admin_tables();
   document.getElementById('table4').style.display='block';
}
document.getElementById('button-5').onclick= () =>{
   clear_admin_tables();
   document.getElementById('table5').style.display='block';
}
document.getElementById('button-6').onclick= () =>{
   clear_admin_tables();
   document.getElementById('table6').style.display='block';
}
document.getElementById('button-7').onclick= () =>{
   clear_admin_tables();
   document.getElementById('table7').style.display='block';
}
document.getElementById('button-8').onclick= () =>{
   clear_admin_tables();
   document.getElementById('table8').style.display='block';
}
document.getElementById('button-9').onclick= () =>{
   clear_admin_tables();
   document.getElementById('table9').style.display='block';
}
document.getElementById('button-10').onclick= () =>{
   clear_admin_tables();
   document.getElementById('table10').style.display='block';
}
document.getElementById('button-11').onclick= () =>{
   clear_admin_tables();
   document.getElementById('table11').style.display='block';
}




