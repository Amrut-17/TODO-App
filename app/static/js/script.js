
const darkfunc = () => {
    let mode = document.body.style.backgroundColor;
    // const heading = document.getElementsByClassName('heading');
    if(mode == 'gray'){
        document.body.style.backgroundColor='white';
        // heading.color='white'
        
    }else{
        document.body.style.backgroundColor='gray';
    }
    
}