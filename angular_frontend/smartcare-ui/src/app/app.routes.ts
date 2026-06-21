import { Routes } from '@angular/router';
import { Treatments } from './pages/treatments/treatments';
import { Appointments } from './pages/appointments/appointments';
import { Doctors } from './pages/doctors/doctors';
// import { BillingServices } from './services/billing';
import { Dashboard } from './pages/dashboard/dashboard';
import { Login } from './pages/login/login';
import { Patients } from './pages/patients/patients';
import { Billing } from './pages/billing/billing';



export const routes: Routes = [
  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full'
  },
  {
    path: 'login',
    component: Login
  },
  {
    path: 'dashboard',
    component: Dashboard
  },
  {
    path: 'patients',
    component: Patients
  },
  {
    path: 'doctors',
    component: Doctors
  },
  {
    path: 'appointments',
    component: Appointments
  },
  {
    path: 'billing',
    component: Billing
  },
  {
    path: 'treatments',
    component: Treatments
  }
];