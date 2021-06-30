import React,{useState} from 'react';
import axios from 'axios';

const Login = ({setUserId}) => {

    const [name,setName] = useState("");
    const [password,setPassword] = useState(""); 

    const getUserId = async () => {
        const data = {
            user_name: name,
            password: password
        }
        const response = await axios.post('http://localhost:8000/user/login/',data);
        //console.log(response);
        setUserId(response.data);
    };


    return (<div classname="container">
        <div className="form-group">
                <lable htmlFor="name">Name:</lable>
                <input type="text"className="form-control" 
                    id="name" name="name" placeholder={name} 
                    value={name} onChange={(e) => setName(e.target.value)} 
                />
            </div>
            <div className="form-group">
                <lable htmlFor="password">Password:</lable>
                <input type="password" className="form-control" 
                    id="password" name="password" placeholder={password}
                    value={password} onChange={(e) => setPassword(e.target.value)} 
                />
            </div>
            <button className="btn btn-success" onClick={getUserId}>Login</button>
    </div>);
};

export default Login;