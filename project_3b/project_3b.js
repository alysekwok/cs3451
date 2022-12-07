// Here are the two new routines that you should add to your ray tracer for Part B

function ambient_light (r, g, b) {
  a_color = new Color(r, g, b);
}

function new_sphere (x, y, z, radius) {
  items.push(new Sphere(x, y, z, radius));
}

// You should swap in your routines from Part A for the placeholder routines below

function reset_scene() {
  lights = [];
  backgroundColor = new Color(0, 0, 0);
  k = 0;
  angle = 0;
  materials = [];
  items = [];
  a_color = new Color(0, 0, 0);
}

function set_background (r, g, b) {
  backgroundColor = new Color(r, g, b);
}

function set_fov (angle) {
  angle *= Math.PI/360;
  k = Math.tan(angle);
}

function new_light (r, g, b, x, y, z) {
  lights.push(new P_Light(r, g, b, x, y, z));
}

function new_material (dr, dg, db,  ar, ag, ab,  sr, sg, sb,  pow,  k_refl) {
  materials.push(new Material(dr, dg, db, ar, ag, ab, sr, sg, sb, pow, k_refl));
}

function new_cylinder (x, y, z, radius, h) {
  items.push(new Cylinder(x, y, z, radius, h));
}

let lights = [];
let materials = [];

let items = [];

//start of classes - OOP structure

class Color {
  constructor(r, g, b) {
    this.r = r;
    this.g = g;
    this.b = b;
  }
}

class Point {
  constructor(x, y, z) {
    this.x = x;
    this.y = y;
    this.z = z;
  }
}

class P_Light {
  constructor(r, g, b, x, y, z) {
    this.color = new Color(r, g ,b);
    this.position = new Point(x, y, z);
  }
}

class Material {
  constructor(dr, dg, db,  ar, ag, ab,  sr, sg, sb,  pow,  k_refl) {
    this.color = new Color(dr, dg, db);
    this.a_color = new Color(ar, ag, ab);
    this.specularColor = new Color(sr, sg, sb);
    this.specularPower = pow;
    this.k_refl = k_refl;
  }
}

class Cylinder {
  constructor(x, y, z, radius, h) {
    // this.base = createVector(x, y, z);
    this.base = new Point(x, y, z);
    this.radius = radius;
    this.h = h;
    this.color = materials[materials.length - 1];
    this.type = 'cylinder';
  }
}

class Sphere {
  constructor(x, y, z, r) {
    this.x = x;
    this.y = y;
    this.z = z;
    this.r = r;
    this.color = materials[materials.length - 1];
    this.type = 'sphere';
  }
}

class Ray {
  constructor(x, y, vector) {
    if (vector) {
      this.origin = vector[0];
      this.dir = vector[1];
    } else {
      let x1 = (x - width / 2) * (2 * k / width);
      let y1 = -1*(y - height / 2) * (2 * k / height);
      this.origin = new Point(0, 0, 0);
      this.dir = new p5.Vector(x1, y1, -1);
    }
  }
}

class Hit {
  constructor(location, normal) {
    this.location = location;
    this.normal = normal;
  }
}

let backgroundColor = new Color(0, 0, 0);
let a_color = new Color(0, 0, 0);

//loops through items in list to see where there is an intersection between ray and item
function intersection(x, y, inputRay, inputObj) {
  let ray;
  if (inputRay != null) {
    ray = inputRay;
  } else {
    ray = new Ray(x, y);
  }
  let closest = Number.MAX_VALUE;
  let Hit_object = null;
  let hit = null;
  //loop through all items
  for (let i = 0; i < items.length; i++) { 
    if (inputObj && inputObj === items[i]) {
      continue;
    }
    //if object is cylinder, finds t values
    if (items[i].type == 'cylinder') {
      let cylinder = items[i];
      let base = cylinder.base;
      
      let dx = ray.dir.x;
      let dz = ray.dir.z;
      let cx = ray.origin.x - base.x;
      let cz = ray.origin.z - base.z;
      let a = dx*dx + dz*dz;
      let b = 2 * (dx * (cx) + dz * (cz));
      let c = (cx)*(cx) + (cz)*(cz) - cylinder.radius*cylinder.radius;

      // calculate discriminant
      if (b*b - 4*a*c < 0) {
        continue;
      }
      
      //comparing t values
      let t1 = (-b + Math.sqrt(b*b - 4*a*c)) / (2*a);
      let t2 = (-b - Math.sqrt(b*b - 4*a*c)) / (2*a);

      // end caps
      let endCap1 = (base.y - ray.origin.y) / ray.dir.y;
      let endCap2 = (base.y - ray.origin.y + cylinder.h ) / ray.dir.y;
      if (!(base.y < ray.origin.y + t1*ray.dir.y && base.y > ray.origin.y + t2*ray.dir.y)) {
        endCap1 = Number.MAX_VALUE;
      }
      if (base.y > ray.origin.y + t2*ray.dir.y - cylinder.h || base.y < ray.origin.y + t1*ray.dir.y - cylinder.h) {
        endCap2 = Number.MAX_VALUE;
      }
      // console.log(endCap1, endCap2);
      let T = Math.min(endCap1, endCap2);
      if (!(base.y < ray.origin.y + t1*ray.dir.y && ray.origin.y + t1*ray.dir.y < base.y + cylinder.h)) {
        t1 = Number.MAX_VALUE;
      }
      if (!(base.y < ray.origin.y + t2*ray.dir.y && ray.origin.y + t2*ray.dir.y < base.y + cylinder.h)) {
        t2 = Number.MAX_VALUE;
      }
      T = Math.max(0, Math.min(endCap1, endCap2, t1, t2));
      T = T == 0 ? Number.MAX_VALUE : T;
      
      if (T < closest && T != Number.MAX_VALUE) {
          closest = T;
          Hit_object = cylinder;
          let pointHit = new Point(ray.origin.x + T*ray.dir.x, ray.origin.y + T*ray.dir.y, ray.origin.z + T*ray.dir.z);
          let normal = new p5.Vector(pointHit.x - base.x, 0, pointHit.z - base.z);
          if (T == endCap1) {
            normal =new p5.Vector(0, -1, 0);           
          } else if (T == endCap2) {
            normal = new p5.Vector(0, 1, 0);
          }  
          normal.normalize();
          hit = new Hit(pointHit, normal);
      }
      //if object is a sphere
    } else {
      let sphere = items[i];
      dx = ray.dir.x;
      dy = ray.dir.y;
      dz = ray.dir.z;
      cx = ray.origin.x - sphere.x;
      cy = ray.origin.y - sphere.y;
      cz = ray.origin.x - sphere.x;
      let a = dx*dx + dy*dy + dz*dz;
      let b = 2 * (dx * (ray.origin.x - sphere.x) + ray.dir.z * (ray.origin.z - sphere.z) + ray.dir.y * (ray.origin.y - sphere.y));
      let c = (ray.origin.x - sphere.x)*(ray.origin.x - sphere.x) + (ray.origin.z - sphere.z)*(ray.origin.z - sphere.z) + (ray.origin.y - sphere.y)*(ray.origin.y - sphere.y) - sphere.r*sphere.r;

      if (b*b - 4*a*c < 0) {
        continue;
      }
      let t1 = (-b + Math.sqrt(b*b - 4*a*c)) / (2*a);
      let t2 = (-b - Math.sqrt(b*b - 4*a*c)) / (2*a);

      T = Math.max(0, Math.min(t1, t2));
      if (T == 0) {
        T = Number.MAX_VALUE;
      }
      if (T < closest && T != Number.MAX_VALUE) {
          closest = T;
          Hit_object = sphere;
          let pointHitx =ray.origin.x + T*ray.dir.x;
          let pointHity =ray.origin.y + T*ray.dir.y;
          let pointHitz =ray.origin.z + T*ray.dir.z;
          let pointHit = new Point(pointHitx, pointHity, pointHitz);
          let normal = new p5.Vector(pointHit.x - sphere.x, pointHit.y - sphere.y, pointHit.z - sphere.z);
          normal.normalize();
          hit = new Hit(pointHit, normal);
      }
    }
  }
  return [Hit_object, hit];
}

function draw_scene() {
  
  noStroke();
  // add your ray creation and scene intersection code here
  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      let [Hit_object, hit] = intersection(x, y);
      let finalColor = getColor(0, Hit_object, hit); // call helper function
      
      let r = finalColor.r;
      let g = finalColor.g;
      let b = finalColor.b;
      fill (r * 255, g * 255, b * 255);
  
      // draw a little rectangle to fill the pixel
      rect (x, y, 1, 1);
    }
  }
}

function getColor(depth, Hit_object, hit) {
  let col = backgroundColor; // initial color setting
  
  if (Hit_object != null) {
     let colorr = Hit_object.color.a_color.r * Hit_object.color.color.r * a_color.r;
     let colorg = Hit_object.color.a_color.g * Hit_object.color.color.g * a_color.g;
     let colorb = Hit_object.color.a_color.b * Hit_object.color.color.b * a_color.b;
     col = new Color(colorr, colorg, colorb);
     
     //reflection
     let N = hit.normal;
     let E = new p5.Vector(-hit.location.x, -hit.location.y, -hit.location.z);
     E.normalize();
     if (depth < 3 && Hit_object.color.k_refl > 0) {
       let nDotE = 2*(N.x*E.x + N.y*E.y + N.z*E.z);
       let RmultN = new p5.Vector(nDotE*N.x, nDotE*N.y, nDotE*N.z);
       let R = new p5.Vector(RmultN.x - E.x, RmultN.y - E.y, RmultN.z - E.z);
       R.normalize();
       
 
       let reflect = [new Point(hit.location.x, hit.location.y, hit.location.z), new p5.Vector(R.x, R.y, R.z)]; 
       let reflectRay = new Ray(0, 0, reflect);
       let [reflectH, reflectHit] = intersection(0, 0, reflectRay, Hit_object);
       if (reflectHit != null) {
         let newColor = getColor(depth+1, reflectH, reflectHit); // recursive call
         col.r += newColor.r * Hit_object.color.k_refl;
         col.g += newColor.g * Hit_object.color.k_refl;
         col.b += newColor.b * Hit_object.color.k_refl;
       } else {
         col.r += backgroundColor.r * Hit_object.color.k_refl;
         col.g += backgroundColor.g * Hit_object.color.k_refl;
         col.b += backgroundColor.b * Hit_object.color.k_refl;
       }
     }
    
    //shadows
    for (let i = 0; i < lights.length; i++) {
      let light = lights[i];

      let lightV = new p5.Vector(light.position.x - hit.location.x, light.position.y - hit.location.y, light.position.z - hit.location.z);
      let eyeV = new p5.Vector(-hit.location.x, -hit.location.y, -hit.location.z);
      lightV.normalize();
      eyeV.normalize();
      let L = new p5.Vector(lightV.x + eyeV.x, lightV.y + eyeV.y, lightV.z + eyeV.z);
      L.normalize();
      let LDot = L.dot(hit.normal);
      let r = lightV.dot(hit.normal);
      if (r < 0) {
        r = 0;
      }
      if (LDot < 0) {
        LDot = 0;
      }
      let shadow = [new Point(hit.location.x, hit.location.y, hit.location.z), new p5.Vector(light.position.x-hit.location.x, light.position.y-hit.location.y, light.position.z-hit.location.z)]; 
      let shadowRay = new Ray(0, 0, shadow);
      let [shadowH, shadowHit] = intersection(0, 0, shadowRay, Hit_object);
      if (shadowHit != null) {
        continue;
      }

      col.r += light.color.r * Hit_object.color.color.r * r + light.color.r * Hit_object.color.specularColor.r * Math.pow(LDot, Hit_object.color.specularPower);
      col.g += light.color.g * Hit_object.color.color.g * r + light.color.g * Hit_object.color.specularColor.g * Math.pow(LDot, Hit_object.color.specularPower);
      col.b += light.color.b * Hit_object.color.color.b * r + light.color.b * Hit_object.color.specularColor.b * Math.pow(LDot, Hit_object.color.specularPower);
    
    }

  }
  return col;
}
  

  // go through all the pixels in the image
  
  



//for (let y = 0; y < height; y++) {
//    for (let x = 0; x < width; x++) {
      
      
     
        
        
//      // add your ray creation and scene intersection code here
//      let [hCylinder, hit] = intersection(x, y);
//      // print(hit);
      
//      var col = backgroundColor;
//      if (hCylinder != null) {
//        col = new Color(hCylinder.color.ambientColor.r * hCylinder.color.color.r * ambientColor.r, hCylinder.color.ambientColor.g * hCylinder.color.color.g * ambientColor.g, hCylinder.color.ambientColor.b * hCylinder.color.color.b * ambientColor.b);
        
        
//        for (let i = 0; i < plights.length; i++) {
//          let light = plights[i];

//          let lightV = new p5.Vector(light.position.x - hit.location.x, light.position.y - hit.location.y, light.position.z - hit.location.z);
//          let eyeV = new p5.Vector(-1*hit.location.x, -1*hit.location.y, -1*hit.location.z);
//          lightV.normalize();
//          eyeV.normalize();
//          let L = new p5.Vector(lightV.x + eyeV.x, lightV.y + eyeV.y, lightV.z + eyeV.z);
//          L.normalize();
//          let LDot = L.dot(hit.normal);
//          let r = lightV.dot(hit.normal);
//          if (r < 0) {
//            r = 0;
//          }
//          if (LDot < 0) {
//            LDot = 0;
//          }

//          let shadow = [new Point(hit.location.x, hit.location.y, hit.location.z), new p5.Vector(light.position.x-hit.location.x, light.position.y-hit.location.y, light.position.z-hit.location.z)]; 
//          let shadowRay = new Ray(0, 0, shadow);
//          let [shadowH, shadowHit] = intersection(0, 0, shadowRay, hCylinder);
//          if (shadowHit != null) {
//            continue;
//          }

//          col.r += light.color.r * hCylinder.color.color.r * r;
//          col.r += light.color.r * hCylinder.color.specularColor.r * Math.pow(LDot, hCylinder.color.specularPower);
//          col.g += light.color.g * hCylinder.color.color.g * r;
//          col.g += light.color.g * hCylinder.color.specularColor.g * Math.pow(LDot, hCylinder.color.specularPower);
//          col.b += light.color.b * hCylinder.color.color.b * r;
//          col.b += light.color.b * hCylinder.color.specularColor.b * Math.pow(LDot, hCylinder.color.specularPower);
//        }

//      }
//      // set the pixel color to the shaded color of the ray
//      let r = col.r;
//      let g = col.g;
//      let b = col.b;
//      fill (r * 255, g * 255, b * 255);

//      // draw a little rectangle to fill the pixel
//      rect (x, y, 1, 1);
      
//    }
//  }
