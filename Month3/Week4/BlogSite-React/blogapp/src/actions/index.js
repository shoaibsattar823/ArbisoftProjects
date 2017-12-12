import axios from 'axios';
import Login from '../containers/login';
// actions
export const ADD_BLOG = 'ADD_BLOG';
export const FETCH_BLOGS = 'FETCH_BLOGS';
export const EDIT_BLOG = 'EDIT_BLOG';
export const FETCH_BLOG_DETAIL = 'FETCH_BLOG_DETAIL';
export const FETCH_TOKEN = 'FETCH_TOKEN';


const ROOT_URL = "http://localhost:8000";


export function fetchToken(data){
  const url = 'http://localhost:8000/obtain_auth_token/';
  const response = axios.post(url, data);
  console.log("response: ", response);
  return {
      type: FETCH_TOKEN,
      payload: response
  };
    // .then(response =>
    //   {
    //     type: FETCH_TOKEN,
    //     payload: response.data.token
    //   }
    // )
}

export function addBlog({data, token}={}){
  console.log('********\n', 'data: ', data, ' Token: ', token, '\n*********')
  const url = `${ROOT_URL}/blogs/`;
  const response = axios.post(url, data, {headers:{
    Authorization : 'Token '+token}
  });

  // return fetchBlogs();
  return {
    type: ADD_BLOG,
    payload: response
  };
    // .then(response => console.log(response))
}

export function fetchBlogs(){
  const url = `${ROOT_URL}/blogs/?format=json`;
  // const url = 'http://api.openweathermap.org/data/2.5/forecast?q=Skardu,us&appid=3f4be8e2d6926fad51510a2874891677';
  const request = axios.get(url);

  return {
    type: FETCH_BLOGS,
    payload: request
  };
}


export function fetchBlogDetail(title) {
  console.log('Inside fetchBlogDetail -- actions');
  const url = `${ROOT_URL}/blogs/${title}/?format=json`;
  const request = axios.get(url);
  return {
    type: FETCH_BLOG_DETAIL,
    payload: request
  };
}
