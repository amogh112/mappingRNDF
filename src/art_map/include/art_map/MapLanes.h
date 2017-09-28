/* -*- mode: C++ -*- */
/*
 *  Copyright (C) 2007, 2010 David Li, Patrick Beeson, Jack O'Quin
 *
 *  License: Modified BSD Software License Agreement
 * 
 *  $Id: 546937d3eb35372e69059ccdf03a83e1bd8af3b0 $
 */

/**  \file
 
     C++ interface for operating on MapLanes polygons.

     \author David Li, Patrick Beeson, Jack O'Quin

 */

#ifndef __MapLanes_h__
#define __MapLanes_h__

#include <math.h>
#include <vector>
#include <stdio.h>

#include <art/UTM.h>
#include <art/error.h>
#include <art/conversions.h>

#include <art_msgs/ArtLanes.h>
#include <art_map/FilteredPolygon.h>
#include <art_map/DrawLanes.h>
#include <art_map/Graph.h>
#include <art_map/PolyOps.h>
#include <art_map/RNDF.h>
#include <art_map/SmoothCurve.h>
#include <art_map/types.h>
#include <art_map/zones.h>

#define MIN_POLY_SIZE 2.5

//#define DEBUGMAP

class MapLanes
{
public:
  MapLanes(float r=-1)
  {
    range = r;
    transition=false;
    trans_index=-1;
  };
  ~MapLanes()
  {
     #ifdef DEBUGMAP
      fclose(debugFile);
     #endif
   };

  int MapRNDF(Graph* _graph, float _max_poly_size=MIN_POLY_SIZE);

  int getAllLanes(art_msgs::ArtLanes *lanes);
  int getLanes(art_msgs::ArtLanes *lanes, MapXY here);
  int getVisionLanes(art_msgs::ArtLanes *lanes, float x, float y, float heading);

  void SetGPS(double centerX, double centerY)
  {
    cX=centerX;
    cY=centerY;
  }

  void SetRobotPos(MapPose pose)
  {
    rX = pose.map.x;
    rY = pose.map.y;
    rOri = pose.yaw;
  }

  //for testing purposes, outputs an image of all polygons
  void testDraw(bool with_trans = false);
  void testDraw(bool with_trans, const ZonePerimeterList &zones);
  void UpdateWithCurrent(int i);

  void UpdatePoly(polyUpdate upPoly, float rX, float rY, float rOri);

private:
  int32_t poly_id_counter;
  std::vector<poly> allPolys;
  std::vector<FilteredPolygon> filtPolys;

  float max_poly_size;

  float range;

  bool transition;
  int trans_index;

  Graph* graph;

  float rX,rY,rOri;

  void MakePolygons();

  poly build_waypoint_poly(const WayPointNode& w1, const WayPointEdge &e,
			   const Point2f& _pt,
			   float time,
			   SmoothCurve& c);

  void MakeLanePolygon(WayPointNode w1, WayPointNode w2, WayPointEdge e,
		       float time1, float time2,
		       SmoothCurve& c,
		       bool new_edge,
		       float ltime1, float ltime2,
		       SmoothCurve& lc,
		       float rtime1, float rtime2,
		       SmoothCurve& rc);

  void MakeTransitionPolygon(WayPointNode w1, WayPointNode w2, WayPointEdge e, 
			     float time1, float time2,
			     SmoothCurve& c);

  void SetFilteredPolygons();

  PolyOps ops;
  
  // File Writing / Reading
  bool WriteToFile(char* fName);
  bool LoadFromFile(char* fName);

  double cX;
  double cY;

#ifdef DEBUGMAP
  // Debugging stuff
  FILE* debugFile;
  void WritePolygonToDebugFile(int poly_id); 
#endif
};

#endif // __MapLanes_h__
