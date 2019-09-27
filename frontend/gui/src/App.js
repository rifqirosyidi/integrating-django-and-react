import React from 'react';
import './App.css';
import 'antd/dist/antd.css'; // or 'antd/dist/antd.less'
import CustomLayout from './containers/Layout';
import Article from './components/Article';

function App() {
  return (
    <div className="App">
     <CustomLayout>
       <Article />
     </CustomLayout>
    </div>
  );
}

export default App;
