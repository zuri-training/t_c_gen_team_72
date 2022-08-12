window.addEventListener('DOMContentLoaded',()=>{
    const path=location.pathname.split('/')[1]
    const patharray=['privacypolicy.html','user.html','collection.html','use.html','disclosure.html','tracking.html','rights.html','finaldetails.html']

    const status=getStatus()
    const pageStatus=patharray.indexOf(path)
    if( pageStatus-page > 1) {
        location.href='/'+ patharray['status']
}
    else{
        

    }

})
function getStatus(){
    const status=localStorage.getitem('status')
    if(status) return Number(status) 
    else{
        localStorage.setItem('status','0')
        return 0
    }


}
function setStatus(value){
    localStorage.setItem('status',value)

}