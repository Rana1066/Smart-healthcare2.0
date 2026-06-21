import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { Auth } from '../../services/auth';

@Component({
  selector: 'app-login',
  imports: [FormsModule],
  templateUrl: './login.html',
  styleUrl: './login.css',
})
export class Login {
username = '';
  password = '';

  constructor(
    private authService: Auth,
    private router: Router
  ) {}

  login() {

    this.authService.login(
      this.username,
      this.password
    ).subscribe({

      next: (response) => {

        localStorage.setItem(
          'access_token',
          response.access
        );

        this.router.navigate(['/dashboard']);
      },

      error: (error: any) => {
        alert('Invalid username or password');
        console.log(error);
      }
    });
  }
}
