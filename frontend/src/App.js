import React from 'react'
import Project from './components/Project.js'
import ToDo from './components/ToDo.js'
import User from './components/User.js'
import LoginForm from './components/Auth.js'
import {BrowserRouter, Route, Switch, Redirect, Link} from 'react-router-dom'
import axios from 'axios'
import Cookies from 'universal-cookie';

const NotFound404 = ({ location }) => {
return (
<div>
<h1>Страница по адресу '{location.pathname}' не найдена</h1>
</div>
)
}

class App extends React.Component {
constructor(props) {
super(props)
this.state = {
'projects': [],
'ToDo': [],
'User': [],
'token': ''

}

set_token(token) {
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({'token': token}, ()=>this.load_data())
    }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }
    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, ()=>this.load_data())
    }

get_token(username, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username,
    password: password})
    .then(response => {
    this.set_token(response.data['token'])
}).catch(error => alert('Неверный логин или пароль'))
}

get_headers() {
    let headers = {
    'Content-Type': 'application/json'
    }
    if (this.is_authenticated())
    {
    headers['Authorization'] = 'Token ' + this.state.token
    }
    return headers
}



    }
load_data() {
    const headers = this.get_headers()
    axios.get('http://127.0.0.1:8000/api/projects/')
        .then(response => {
            this.setState({projects: response.data})
        }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/ToDo/')
        .then(response => {
            this.setState({ToDo: response.data})
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/users/')
        .then(response => {
            this.setState({users: response.data})
        }).catch(error => console.log(error))
    }

    componentDidMount() {
   this.get_token_from_storage()
    }

    render() {
        return (
            <div className="App">
            <BrowserRouter>
            <nav>
            <ul>
            <li>
            <Link to='/projects'>Projects</Link>
            </li>
            <li>
            <Link to='/users'>Users</Link>
            </li>
            <li>
            <Link to='/ToDo'>ToDo</Link>
            </li>
            <li>
            <Link to='/login'>Login</Link>
            </li>
            </ul>
            </nav>
            <Switch>
                <Route exact path='/' component={() => <ToDo
items={this.state.authors} />} />
                <Route exact path='/ToDo' component={() => <Projects
items={this.state.books} />} />
                <Route exact path='/login' component={() => <LoginForm
get_token={(username, password) => this.get_token(username, password)} />} />
            <Route path="/todo/:id">
                <ToDo items={this.state.todo} />
            </Route>
            <Redirect from='/todo' to='/' />
            <Route component={NotFound404} />
            </Switch>
            </BrowserRouter>
            </div>
        )
    }
}
export default App;


get_token(username, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username,
password: password})
    .then(response => {
        console.log(response.data)
    }).catch(error => alert('Неверный логин или пароль'))
    }

