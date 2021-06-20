import React from 'react';
import ToDo from './components/ToDo';
import Completed from './components/Completed';
import InProgress from './components/InProgress';

const App = () => {
    return (<div className="mx-5">
        <div className="row">
            <div className="col-4"><ToDo /></div>
            <div className="col-4"><InProgress /></div>
            <div className="col-4"><Completed /></div>
        </div>
    </div>);
};

export default App;