import React, { useState } from 'react';

const SignUp = () => {
    const [name,setName] = useState("");
    const [email,setEmail] = useState("");
    const [recoveryemail,setRecoveryEmail]=useState("");
    const [password,setPassword] = useState("");    
    return(<div>
        <div className="container">
            <div className="form-group">
                <lable htmlFor="name">Name:</lable>
                <input type="text"className="form-control" 
                    id="name" name="name" placeholder={name} 
                    value={name} onChange={(e) => setName(e.target.value)} 
                />
            </div>
            <div className="form-group">
                <lable htmlFor="email">Email:</lable>
                <input type="email" className="form-control" 
                    id="email" name="email" placeholder={email}
                    value={email} onChange={(e) => setEmail(e.target.value)} 
                />
            </div>
            <div className="form-group">
                <lable htmlFor="recoveryemail">Recovery Email:</lable>
                <input type="email" className="form-control" 
                    id="recoveryemail" name="recoveryemail" placeholder={recoveryemail}
                    value={recoveryemail} onChange={(e) => setRecoveryEmail(e.target.value)} 
                />
            </div>
            <div className="form-group">
                <lable htmlFor="password">Password:</lable>
                <input type="password" className="form-control" 
                    id="password" name="password" placeholder={password}
                    value={password} onChange={(e) => setPassword(e.target.value)} 
                />
            </div>

        </div>
    </div>);
};

export default SignUp;