
var passw=document.getElementById('psw');
var flag=1;

function check(arg)
{
if(arg.value.length>0)
{
if(arg.value!=passw.value)
{
document.getElementById('alert').innerTEXT="Password does not match";
flag=0;
}
else
{
document.getElementById('alert').innerTEXT="Password matched";
flag=1;
}


}
else
{
document.getElementById('alert').innerTEXT="Please confirm your password";
flag=0;
}
}
function validate(){
if(flag==1)
{
return true
}
else
{
return false
}
}


