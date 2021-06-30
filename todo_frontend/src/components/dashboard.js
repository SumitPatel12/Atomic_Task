import React from 'react';
import ToDo from './ToDo';
import InProgress from './InProgress';
import Completed from './Completed';

const Dashboard = ({ user_id,setUserId }) => {
    return (<div className="container"><div className="row">
    <div className="col-4"><ToDo user_id = {user_id}/></div>
    <div className="col-4"><InProgress user_id = {user_id} /></div>
    <div className="col-4"><Completed user_id = {user_id} /></div>    
</div>
<button className="btn btn-danger" onClick={() => setUserId("")}>Log out!!</button>
</div>);
}

export default Dashboard;