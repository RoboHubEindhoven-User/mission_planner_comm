// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: service_area.proto

#ifndef PROTOBUF_service_5farea_2eproto__INCLUDED
#define PROTOBUF_service_5farea_2eproto__INCLUDED

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 2006000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 2006001 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)

namespace mission_protobuf {

// Internal implementation detail -- do not call these.
void  protobuf_AddDesc_service_5farea_2eproto();
void protobuf_AssignDesc_service_5farea_2eproto();
void protobuf_ShutdownFile_service_5farea_2eproto();

class ServiceArea;

// ===================================================================

class ServiceArea : public ::google::protobuf::Message {
 public:
  ServiceArea();
  virtual ~ServiceArea();

  ServiceArea(const ServiceArea& from);

  inline ServiceArea& operator=(const ServiceArea& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _unknown_fields_;
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return &_unknown_fields_;
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const ServiceArea& default_instance();

  void Swap(ServiceArea* other);

  // implements Message ----------------------------------------------

  ServiceArea* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const ServiceArea& from);
  void MergeFrom(const ServiceArea& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const;
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  public:
  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // required string description = 1;
  inline bool has_description() const;
  inline void clear_description();
  static const int kDescriptionFieldNumber = 1;
  inline const ::std::string& description() const;
  inline void set_description(const ::std::string& value);
  inline void set_description(const char* value);
  inline void set_description(const char* value, size_t size);
  inline ::std::string* mutable_description();
  inline ::std::string* release_description();
  inline void set_allocated_description(::std::string* description);

  // required double length = 2;
  inline bool has_length() const;
  inline void clear_length();
  static const int kLengthFieldNumber = 2;
  inline double length() const;
  inline void set_length(double value);

  // required double width = 3;
  inline bool has_width() const;
  inline void clear_width();
  static const int kWidthFieldNumber = 3;
  inline double width() const;
  inline void set_width(double value);

  // required double height = 4;
  inline bool has_height() const;
  inline void clear_height();
  static const int kHeightFieldNumber = 4;
  inline double height() const;
  inline void set_height(double value);

  // required double diameter = 5;
  inline bool has_diameter() const;
  inline void clear_diameter();
  static const int kDiameterFieldNumber = 5;
  inline double diameter() const;
  inline void set_diameter(double value);

  // required double tilt_angle = 6;
  inline bool has_tilt_angle() const;
  inline void clear_tilt_angle();
  static const int kTiltAngleFieldNumber = 6;
  inline double tilt_angle() const;
  inline void set_tilt_angle(double value);

  // @@protoc_insertion_point(class_scope:mission_protobuf.ServiceArea)
 private:
  inline void set_has_description();
  inline void clear_has_description();
  inline void set_has_length();
  inline void clear_has_length();
  inline void set_has_width();
  inline void clear_has_width();
  inline void set_has_height();
  inline void clear_has_height();
  inline void set_has_diameter();
  inline void clear_has_diameter();
  inline void set_has_tilt_angle();
  inline void clear_has_tilt_angle();

  ::google::protobuf::UnknownFieldSet _unknown_fields_;

  ::google::protobuf::uint32 _has_bits_[1];
  mutable int _cached_size_;
  ::std::string* description_;
  double length_;
  double width_;
  double height_;
  double diameter_;
  double tilt_angle_;
  friend void  protobuf_AddDesc_service_5farea_2eproto();
  friend void protobuf_AssignDesc_service_5farea_2eproto();
  friend void protobuf_ShutdownFile_service_5farea_2eproto();

  void InitAsDefaultInstance();
  static ServiceArea* default_instance_;
};
// ===================================================================


// ===================================================================

// ServiceArea

// required string description = 1;
inline bool ServiceArea::has_description() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void ServiceArea::set_has_description() {
  _has_bits_[0] |= 0x00000001u;
}
inline void ServiceArea::clear_has_description() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void ServiceArea::clear_description() {
  if (description_ != &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    description_->clear();
  }
  clear_has_description();
}
inline const ::std::string& ServiceArea::description() const {
  // @@protoc_insertion_point(field_get:mission_protobuf.ServiceArea.description)
  return *description_;
}
inline void ServiceArea::set_description(const ::std::string& value) {
  set_has_description();
  if (description_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    description_ = new ::std::string;
  }
  description_->assign(value);
  // @@protoc_insertion_point(field_set:mission_protobuf.ServiceArea.description)
}
inline void ServiceArea::set_description(const char* value) {
  set_has_description();
  if (description_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    description_ = new ::std::string;
  }
  description_->assign(value);
  // @@protoc_insertion_point(field_set_char:mission_protobuf.ServiceArea.description)
}
inline void ServiceArea::set_description(const char* value, size_t size) {
  set_has_description();
  if (description_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    description_ = new ::std::string;
  }
  description_->assign(reinterpret_cast<const char*>(value), size);
  // @@protoc_insertion_point(field_set_pointer:mission_protobuf.ServiceArea.description)
}
inline ::std::string* ServiceArea::mutable_description() {
  set_has_description();
  if (description_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    description_ = new ::std::string;
  }
  // @@protoc_insertion_point(field_mutable:mission_protobuf.ServiceArea.description)
  return description_;
}
inline ::std::string* ServiceArea::release_description() {
  clear_has_description();
  if (description_ == &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    return NULL;
  } else {
    ::std::string* temp = description_;
    description_ = const_cast< ::std::string*>(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
    return temp;
  }
}
inline void ServiceArea::set_allocated_description(::std::string* description) {
  if (description_ != &::google::protobuf::internal::GetEmptyStringAlreadyInited()) {
    delete description_;
  }
  if (description) {
    set_has_description();
    description_ = description;
  } else {
    clear_has_description();
    description_ = const_cast< ::std::string*>(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  }
  // @@protoc_insertion_point(field_set_allocated:mission_protobuf.ServiceArea.description)
}

// required double length = 2;
inline bool ServiceArea::has_length() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void ServiceArea::set_has_length() {
  _has_bits_[0] |= 0x00000002u;
}
inline void ServiceArea::clear_has_length() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void ServiceArea::clear_length() {
  length_ = 0;
  clear_has_length();
}
inline double ServiceArea::length() const {
  // @@protoc_insertion_point(field_get:mission_protobuf.ServiceArea.length)
  return length_;
}
inline void ServiceArea::set_length(double value) {
  set_has_length();
  length_ = value;
  // @@protoc_insertion_point(field_set:mission_protobuf.ServiceArea.length)
}

// required double width = 3;
inline bool ServiceArea::has_width() const {
  return (_has_bits_[0] & 0x00000004u) != 0;
}
inline void ServiceArea::set_has_width() {
  _has_bits_[0] |= 0x00000004u;
}
inline void ServiceArea::clear_has_width() {
  _has_bits_[0] &= ~0x00000004u;
}
inline void ServiceArea::clear_width() {
  width_ = 0;
  clear_has_width();
}
inline double ServiceArea::width() const {
  // @@protoc_insertion_point(field_get:mission_protobuf.ServiceArea.width)
  return width_;
}
inline void ServiceArea::set_width(double value) {
  set_has_width();
  width_ = value;
  // @@protoc_insertion_point(field_set:mission_protobuf.ServiceArea.width)
}

// required double height = 4;
inline bool ServiceArea::has_height() const {
  return (_has_bits_[0] & 0x00000008u) != 0;
}
inline void ServiceArea::set_has_height() {
  _has_bits_[0] |= 0x00000008u;
}
inline void ServiceArea::clear_has_height() {
  _has_bits_[0] &= ~0x00000008u;
}
inline void ServiceArea::clear_height() {
  height_ = 0;
  clear_has_height();
}
inline double ServiceArea::height() const {
  // @@protoc_insertion_point(field_get:mission_protobuf.ServiceArea.height)
  return height_;
}
inline void ServiceArea::set_height(double value) {
  set_has_height();
  height_ = value;
  // @@protoc_insertion_point(field_set:mission_protobuf.ServiceArea.height)
}

// required double diameter = 5;
inline bool ServiceArea::has_diameter() const {
  return (_has_bits_[0] & 0x00000010u) != 0;
}
inline void ServiceArea::set_has_diameter() {
  _has_bits_[0] |= 0x00000010u;
}
inline void ServiceArea::clear_has_diameter() {
  _has_bits_[0] &= ~0x00000010u;
}
inline void ServiceArea::clear_diameter() {
  diameter_ = 0;
  clear_has_diameter();
}
inline double ServiceArea::diameter() const {
  // @@protoc_insertion_point(field_get:mission_protobuf.ServiceArea.diameter)
  return diameter_;
}
inline void ServiceArea::set_diameter(double value) {
  set_has_diameter();
  diameter_ = value;
  // @@protoc_insertion_point(field_set:mission_protobuf.ServiceArea.diameter)
}

// required double tilt_angle = 6;
inline bool ServiceArea::has_tilt_angle() const {
  return (_has_bits_[0] & 0x00000020u) != 0;
}
inline void ServiceArea::set_has_tilt_angle() {
  _has_bits_[0] |= 0x00000020u;
}
inline void ServiceArea::clear_has_tilt_angle() {
  _has_bits_[0] &= ~0x00000020u;
}
inline void ServiceArea::clear_tilt_angle() {
  tilt_angle_ = 0;
  clear_has_tilt_angle();
}
inline double ServiceArea::tilt_angle() const {
  // @@protoc_insertion_point(field_get:mission_protobuf.ServiceArea.tilt_angle)
  return tilt_angle_;
}
inline void ServiceArea::set_tilt_angle(double value) {
  set_has_tilt_angle();
  tilt_angle_ = value;
  // @@protoc_insertion_point(field_set:mission_protobuf.ServiceArea.tilt_angle)
}


// @@protoc_insertion_point(namespace_scope)

}  // namespace mission_protobuf

#ifndef SWIG
namespace google {
namespace protobuf {


}  // namespace google
}  // namespace protobuf
#endif  // SWIG

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_service_5farea_2eproto__INCLUDED
