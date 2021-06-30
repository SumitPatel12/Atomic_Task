import React,{useState} from 'react';
import {BrowserRouter as Router, Switch,Route, Redirect} from 'react-router-dom';

import Dashboard from './components/dashboard';
import SignUp from './components/SignUp';
import Login from './components/Login';

const App = () => {

    const [userid,setUserId] = useState("");
    return (<div>
        <Router>
        <Switch>
            <Route exact path='/' 
            render = {props => userid.length !== 0 
            ? (<Dashboard {...props} user_id={userid} setUserId={setUserId} />):
            (<Redirect to='/login' />)}/>
            
            <Route path='/login'
            render ={props => userid.length === 0 ? 
            <Login {...props} setUserId={setUserId} /> : 
            <Redirect to='/' />} />
            
            <Route path='/signup'>
                <SignUp />
            </Route>                
            </Switch>

        </Router>
    </div>);     
        
};

export default App;