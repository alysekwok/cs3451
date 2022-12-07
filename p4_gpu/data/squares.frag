// Fragment shader

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_LIGHT_SHADER

// These values come from the vertex shader
varying vec4 vertColor;
varying vec3 vertNormal;
varying vec3 vertLightDir;
varying vec4 vertTexCoord;

void main() { 

  // diffuse_color = vec4(1.0, 0.0, 0.0, 1.0);
  float lenSquare = 1.0/7.0;
  float spacing = lenSquare/4.0;
  float c = cos(radians(45));
  float s = sin(radians(45));
  mat2 rotationMatrix = mat2(c, -s, s, c);
  vec2 tempCoord = vec2(vertTexCoord.x, vertTexCoord.y);
  tempCoord = rotationMatrix * tempCoord;
  tempCoord = tempCoord + vec2(-0.2,0.5);

  vec2 squareCenter = vec2(0.5, lenSquare);
  int alpha = 1;
  if (tempCoord.x > squareCenter.x - (lenSquare/2.0) && tempCoord.x < squareCenter.x + (lenSquare/2.0)) {
    if (tempCoord.y > squareCenter.y - (lenSquare/2.0) && tempCoord.y < squareCenter.y + (lenSquare/2.0)) {
      alpha = 0; 
    }
  }
  gl_FragColor = vec4(0, 1, 1, alpha);

 
 

  for (int i = 0; i < 4; i++) {
    squareCenter.x = 0.5;
    squareCenter.y = lenSquare;
    if(i == 0 || i == 2) {
      if (i == 0) {
        squareCenter.x = 0.5 + lenSquare + spacing;
      } else {
        squareCenter.x = 0.5 - lenSquare - spacing;
      }
      for (int j = 0; j < 3; j++) {
        squareCenter.y = squareCenter.y + lenSquare + spacing;
        if (tempCoord.x > squareCenter.x - (lenSquare/2.0) && tempCoord.x < squareCenter.x + (lenSquare/2.0)) {
          if (tempCoord.y > squareCenter.y - (lenSquare/2.0) && tempCoord.y < squareCenter.y + (lenSquare/2.0)) {
            alpha = 0; 
          }
        }
      gl_FragColor = vec4(0, 1, 1, alpha);
      }
    }
    if (i == 1) {
      for (int j = 0; j < 4; j++) {
        squareCenter.y = squareCenter.y + lenSquare + spacing;
        if (tempCoord.x > squareCenter.x - (lenSquare/2.0) && tempCoord.x < squareCenter.x + (lenSquare/2.0)) {
          if (tempCoord.y > squareCenter.y - (lenSquare/2.0) && tempCoord.y < squareCenter.y + (lenSquare/2.0)) {
            alpha = 0; 
          }
        }
      gl_FragColor = vec4(0, 1, 1, alpha);
      }
    } 
    if (i == 3) {
      squareCenter.x = 0.5 - (2 * lenSquare) - (2*spacing);
      squareCenter.y = squareCenter.y + (2*lenSquare) + (2*spacing);
      if (tempCoord.x > squareCenter.x - (lenSquare/2.0) && tempCoord.x < squareCenter.x + (lenSquare/2.0)) {
        if (tempCoord.y > squareCenter.y - (lenSquare/2.0) && tempCoord.y < squareCenter.y + (lenSquare/2.0)) {
          alpha = 0; 
        }
      }
    gl_FragColor = vec4(0, 1, 1, alpha);  

    squareCenter.x = 0.5 + (2 * lenSquare) + (2*spacing);
    if (tempCoord.x > squareCenter.x - (lenSquare/2.0) && tempCoord.x < squareCenter.x + (lenSquare/2.0)) {
        if (tempCoord.y > squareCenter.y - (lenSquare/2.0) && tempCoord.y < squareCenter.y + (lenSquare/2.0)) {
          alpha = 0; 
        }
      }
    gl_FragColor = vec4(0, 1, 1, alpha);  
    }

  }
  

}
        


